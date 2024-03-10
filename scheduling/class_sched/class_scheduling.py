from random import shuffle, choice
from datetime import datetime
from .models import *
import random

"""
# Function to check instructor availability for a given time slot
def is_instructor_available(instructor, day, start_time, end_time):
    instructor_type = Instructor.status
    # Permanent, Temporary, Full-time instructors can work from 7am to 8pm
    if instructor_type in ("Permanent", "Temporary", "Full-Time"):
        if (
            datetime.strptime(start_time, "%H:%M") >= datetime.strptime("7:00", "%H:%M")
        ) and (
            datetime.strptime(end_time, "%H:%M") <= datetime.strptime("20:00", "%H:%M")
        ):
            return True
    # Part-time instructors can only work from 5pm to 8pm
    elif instructor_type == "Part-Time":
        if (
            datetime.strptime(start_time, "%H:%M")
            >= datetime.strptime("17:00", "%H:%M")
        ) and (
            datetime.strptime(end_time, "%H:%M") <= datetime.strptime("20:00", "%H:%M")
        ):
            return True
    return False


def is_room_available(room, course_type, day, start_time, end_time):
    # Check if room belongs to the same college as the course
    if room.college != Course.college:
        return False
    # Check room type compatibility
    if course_type == "Lec" and room.room_type == "Lecture":
        return True
    elif course_type == "Lab and Lec" and room.room_type == "Lab and Lec":
        return True
    return False


# Function to check for time slot conflicts for a class
def has_time_slot_conflict(class_schedule, all_schedules):
    for other_schedule in all_schedules:
        if (
            class_schedule.room == other_schedule.room
            and class_schedule.day == other_schedule.day
            and not (
                datetime.strptime(class_schedule.end_time, "%H:%M")
                <= datetime.strptime(other_schedule.start_time, "%H:%M")
                or datetime.strptime(other_schedule.end_time, "%H:%M")
                <= datetime.strptime(class_schedule.start_time, "%H:%M")
            )
        ):
            return True
    return False


# Function to calculate the fitness score of a chromosome (schedule)
def calculate_fitness(chromosome, all_courses):
    fitness_score = 0
    # Iterate through each class in the schedule (chromosome)
    for class_schedule in chromosome:
        course = class_schedule[0]  # Assuming course is at index 0 in chromosome
        instructor = class_schedule[1]
        room = class_schedule[2]
        day = class_schedule[3]
        start_time = class_schedule[4]
        end_time = class_schedule[5]

        # Check instructor availability violation
        if not is_instructor_available(instructor, day, start_time, end_time):
            fitness_score -= 1

        # Check room availability violation
        if not is_room_available(room, course.type, day, start_time, end_time):
            fitness_score -= 1

        # Check lunch break violation (12:00 pm - 1:00 pm)
        if datetime.strptime(start_time, "%H:%M") >= datetime.strptime(
            "12:00", "%H:%M"
        ) and datetime.strptime(end_time, "%H:%M") <= datetime.strptime(
            "13:00", "%H:%M"
        ):
            fitness_score -= 1

        # Check time slot conflicts
        if has_time_slot_conflict(class_schedule, all_schedules):
            fitness_score -= 1

    # Additional logic can be added to reward specific preferences (e.g., minimizing gaps)
    return fitness_score


def generate_random_chromosome(all_courses, all_instructors, all_rooms, all_weeks):
    chromosome = []
    for course in all_courses:
        # Select a random instructor who teaches the course (from InstructorCourse model)
        instructor_candidates = list(
            course.instructorcourse_set.all()
        )  # Get instructors for the course
        if instructor_candidates:
            instructor = choice(instructor_candidates)  # Choose a random instructor
        else:
            # Handle case where no instructor is assigned to the course (raise error or assign None)
            raise ValueError(f"No instructor assigned to course: {course.course_name}")

        # Select a random room with compatible type for the course
        available_rooms = [
            room
            for room in all_rooms
            if is_room_available(room, course.type, None, None, None)
        ]
        room = choice(available_rooms)  # Choose a random available room

        # Select a random day from all_weeks
        day = choice(all_weeks).day

        # Calculate total duration based on course credits and hours (assuming hours per week)
        total_duration_minutes = int(course.credits) * 60  # Assuming 1 credit = 1 hour
        if (
            course.hours != course.credits
        ):  # Account for courses with different hours per week
            total_duration_minutes += (int(course.hours) - int(course.credits)) * 60

        # Generate random start time within available instructor and room schedule
        start_time_minutes = None
        while not start_time_minutes:
            # Generate random time within instructor's working hours (adjusted for course duration)
            random_start_minute = random.randint(
                (7 * 60) - total_duration_minutes,  # 7:00 AM in minutes
                (19 * 60)  # 7:00 PM in minutes (adjust for part-time instructors)
                - total_duration_minutes,
            )
            # Check if instructor is available for this time slot and room is available for the day
            if is_instructor_available(
                instructor,
                day,
                f"{random_start_minute // 60:02d}:{random_start_minute % 60:02d}",
                f"{((random_start_minute + total_duration_minutes) // 60):02d}:{((random_start_minute + total_duration_minutes) % 60):02d}",
            ) and is_room_available(
                room,
                course.type,
                day,
                f"{random_start_minute // 60:02d}:{random_start_minute % 60:02d}",
                f"{((random_start_minute + total_duration_minutes) // 60):02d}:{((random_start_minute + total_duration_minutes) % 60):02d}",
            ):
                start_time_minutes = random_start_minute

        # Convert minutes to formatted time string
        start_time = f"{start_time_minutes // 60:02d}:{start_time_minutes % 60:02d}"
        end_time = f"{((start_time_minutes + total_duration_minutes) // 60):02d}:{((start_time_minutes + total_duration_minutes) % 60):02d}"

        # Add class details to the chromosome
        chromosome.append([course, instructor, room, day, start_time, end_time])

    return chromosome


def roulette_wheel_selection(population):
    # Calculate total fitness of all chromosomes
    total_fitness = sum(
        calculate_fitness(chromosome, all_courses) for chromosome in population
    )

    # Calculate selection probabilities for each chromosome
    selection_probabilities = [
        calculate_fitness(chromosome, all_courses) / total_fitness
        for chromosome in population
    ]

    # Create a roulette wheel using probabilities (higher fitness = larger slice)
    wheel = sum(selection_probabilities) * np.random.rand(*len(selection_probabilities))

    # Spin the roulette and select a chromosome
    for i, probability in enumerate(selection_probabilities):
        wheel -= probability
        if wheel <= 0:
            return population[i]

    # Handle potential edge cases (shouldn't occur frequently)
    return random.choice(population)


def single_point_crossover(parent1, parent2):
    crossover_point = random.randint(
        1, len(parent1) - 1
    )  # Choose a random crossover point (excluding first and last elements)
    offspring1 = parent1[:crossover_point] + parent2[crossover_point:]
    offspring2 = parent2[:crossover_point] + parent1[crossover_point:]
    return offspring1, offspring2


def mutation(chromosome, mutation_rate):
    for i in range(1, len(chromosome)):  # Skip the first element (course)
        if random.random() < mutation_rate:
            # Randomly choose another element in the chromosome to swap with
            swap_index = random.randint(1, len(chromosome) - 1)
            chromosome[i], chromosome[swap_index] = (
                chromosome[swap_index],
                chromosome[i],
            )
    return chromosome


def genetic_algorithm(
    all_courses, all_instructors, all_rooms, all_weeks, population_size, generations
):
    population = [
        generate_random_chromosome(all_courses, all_instructors, all_rooms, all_weeks)
        for _ in range(population_size)
    ]

    for generation in range(generations):
        # Selection
        selected_parents = [
            roulette_wheel_selection(population) for _ in range(population_size)
        ]

        # Crossover
        offspring = []
        for i in range(0, population_size, 2):  # Process parents in pairs
            offspring1, offspring2 = single_point_crossover(
                selected_parents[i], selected_parents[i + 1]
            )
            offspring.extend([offspring1, offspring2])

        # Mutation
        mutated_offspring = [
            mutation(chromosome, mutation_rate) for chromosome in offspring
        ]

        # Combine parents and offspring for next generation
        population = selected_parents + mutated_offspring

    # Find the chromosome with the highest fitness score
    best_schedule = max(
        population, key=lambda chromosome: calculate_fitness(chromosome, all_courses)
    )
    return best_schedule


# Example usage (replace with your actual data retrieval logic)
all_courses = Course.objects.all()
all_instructors = Instructor.objects.all()
all_rooms = Room.objects.all()
all_weeks = Week.objects.all()

population_size = 100
generations = 50

best_schedule = genetic_algorithm(
    all_courses, all_instructors, all_rooms, all_weeks, population_size, generations
)

"""
