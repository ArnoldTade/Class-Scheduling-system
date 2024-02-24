import random
from collections import defaultdict

# Import your Django models
from class_sched.models import Instructor, Room, Course, ClassSchedule

# Constants
MAX_GENERATIONS = 100
POPULATION_SIZE = 50
MUTATION_RATE = 0.1

# Genetic Algorithm Functions


def generate_random_schedule():
    # Retrieve all instructors and rooms
    instructors = list(Instructor.objects.all())  # Convert queryset to list
    rooms = list(Room.objects.all())  # Convert queryset to list

    # Print lengths of instructors and rooms for debugging
    print("Number of instructors:", len(instructors))
    print("Number of rooms:", len(rooms))

    # Check if lists are empty
    if not instructors or not rooms:
        return []  # Return an empty schedule if no instructors or rooms are available

    # Initialize an empty schedule
    schedule = []

    # Generate schedules for each instructor
    for instructor in instructors:
        # Determine instructor availability based on status
        if instructor.status == "Fulltime":
            available_times = ["8:00am-12:00pm", "1:00pm-5:00pm"]
        elif instructor.status == "Part time":
            available_times = ["5:00pm-8:00pm"]
        else:
            # Handle other status cases if needed
            available_times = []

        # Generate a random course for the instructor
        courses = Course.objects.all().filter(college=instructor.college)
        if courses:
            course = random.choice(courses)
        else:
            continue  # Skip this instructor if no courses available

        # Generate a random room
        room = random.choice(rooms)

        # Generate random start and end times
        start_time = random.choice(available_times)
        end_time = start_time.split("-")[1]  # Get the end time from the available slot

        # Generate random days of the week
        days_of_week = "".join(
            random.sample(["M", "T", "W", "Th", "F"], k=random.randint(1, 5))
        )

        # Generate semester and year (you may need to adjust this based on your requirements)
        semester = random.choice(["Spring", "Summer", "Fall"])
        year = random.choice(["2023", "2024", "2025"])

        # Create a schedule entry and add it to the schedule
        schedule_entry = {
            "course": course,
            "instructor": instructor,
            "room": room,
            "start_time": start_time,
            "end_time": end_time,
            "days_of_week": days_of_week,
            "semester": semester,
            "year": year,
        }
        schedule.append(schedule_entry)

    return schedule


def fitness(schedule):
    # Initialize fitness score
    fitness_score = 0

    # Check for conflicts (two classes scheduled in the same room at the same time)
    room_schedule = defaultdict(list)
    for entry in schedule:
        room_schedule[
            (
                entry["room"],
                entry["days_of_week"],
                entry["start_time"],
                entry["end_time"],
            )
        ].append(entry)

    for entries in room_schedule.values():
        if len(entries) > 1:
            # Conflict detected
            fitness_score -= len(entries) ** 2  # Penalize conflicts quadratically

    # Check for instructor availability
    for entry in schedule:
        if entry["instructor"].status == "Fulltime":
            if entry["start_time"] not in ["8:00am-12:00pm", "1:00pm-5:00pm"]:
                fitness_score -= 1  # Penalize full-time instructor for teaching outside their availability
        elif entry["instructor"].status == "Part time":
            if entry["start_time"] not in ["5:00pm-8:00pm"]:
                fitness_score -= 1  # Penalize part-time instructor for teaching outside their availability
        # You can add more conditions for other instructor statuses if needed

    # Check for course type constraints
    for entry in schedule:
        if entry["course"].type == "Lecture" and "Lab" in entry["room"].room_name:
            fitness_score -= 1  # Penalize for scheduling a lecture in a lab room

    # Additional fitness evaluations based on your specific constraints can be added here

    return fitness_score


def crossover(schedule1, schedule2):
    # Perform crossover between two schedules
    # Choose a random crossover point
    crossover_point = random.randint(1, min(len(schedule1), len(schedule2)) - 1)

    # Create a new child schedule
    child_schedule = []

    # Add entries from schedule1 up to the crossover point
    child_schedule.extend(schedule1[:crossover_point])

    # Add entries from schedule2 after the crossover point, avoiding duplicates
    for entry in schedule2[crossover_point:]:
        if entry not in child_schedule:
            child_schedule.append(entry)

    return child_schedule


def mutate(schedule):
    # Perform mutation on a schedule
    mutated_schedule = schedule[
        :
    ]  # Create a copy of the original schedule to avoid modifying it directly

    # Randomly select a schedule entry to mutate
    index_to_mutate = random.randint(0, len(mutated_schedule) - 1)
    entry_to_mutate = mutated_schedule[index_to_mutate]

    # Apply mutation based on the type of change (e.g., change room, modify timings, etc.)
    if random.random() < 0.5:  # 50% chance of changing room
        # Retrieve all rooms
        rooms = Room.objects.all()
        # Choose a random room different from the current room
        new_room = random.choice(rooms.exclude(id=entry_to_mutate["room"].id))
        mutated_schedule[index_to_mutate]["room"] = new_room

    else:  # 50% chance of modifying timings
        # Modify start time or end time randomly
        if random.random() < 0.5:  # 50% chance of modifying start time
            new_start_time = (
                "8:00am-12:00pm" if random.random() < 0.5 else "1:00pm-5:00pm"
            )
            mutated_schedule[index_to_mutate]["start_time"] = new_start_time
        else:  # 50% chance of modifying end time
            new_end_time = (
                "8:00am-12:00pm" if random.random() < 0.5 else "1:00pm-5:00pm"
            )
            mutated_schedule[index_to_mutate]["end_time"] = new_end_time

    return mutated_schedule


def generate_initial_population():
    # Generate an initial population of schedules
    population = []
    for _ in range(POPULATION_SIZE):
        schedule = generate_random_schedule()
        population.append(schedule)
    return population


def select_parents(population):
    # Select parents based on tournament selection
    # This function should select two schedules with high fitness values

    # Set the tournament size (number of schedules to compete against each other)
    tournament_size = 5

    # Randomly select tournament_size schedules from the population
    tournament_contestants = random.sample(population, tournament_size)

    # Evaluate the fitness of each contestant
    contestant_fitness = [fitness(schedule) for schedule in tournament_contestants]

    # Select the two schedules with the highest fitness values as parents
    parent_indices = sorted(
        range(len(contestant_fitness)),
        key=lambda i: contestant_fitness[i],
        reverse=True,
    )[:2]
    parent1, parent2 = (
        tournament_contestants[parent_indices[0]],
        tournament_contestants[parent_indices[1]],
    )

    return parent1, parent2


def genetic_algorithm():
    # Main genetic algorithm loop
    population = generate_initial_population()

    for generation in range(MAX_GENERATIONS):
        # Evaluate fitness of the population
        fitness_scores = [(schedule, fitness(schedule)) for schedule in population]

        # Select parents
        parents = select_parents(population)

        # Perform crossover and mutation to create new generation
        offspring = []
        for _ in range(POPULATION_SIZE // 2):
            child1 = crossover(parents[0], parents[1])
            child2 = crossover(parents[1], parents[0])
            offspring.extend([mutate(child1), mutate(child2)])

        # Replace old population with new generation
        population = offspring

    # Store the best schedule in the ClassSchedule model
    best_schedule = max(population, key=fitness)
    store_schedule(best_schedule)


def store_schedule(schedule):
    # Store the generated schedule in the ClassSchedule model
    for entry in schedule:
        class_schedule = ClassSchedule(
            course=entry["course"],
            instructor=entry["instructor"],
            room=entry["room"],
            start_time=entry["start_time"],
            end_time=entry["end_time"],
            days_of_week=entry["days_of_week"],
            semester=entry["semester"],
            year=entry["year"],
        )
        class_schedule.save()
