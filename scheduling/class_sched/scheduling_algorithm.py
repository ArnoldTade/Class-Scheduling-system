import random

# Import your Django models
from class_sched.models import Instructor, Room, Course, ClassSchedule
from .models import ClassSchedule
from datetime import datetime, date, timedelta


def generate_population(size):
    population = []
    for _ in range(size):
        schedule = []
        for course in Course.objects.all():
            instructors = Instructor.objects.filter(role="Instructor")
            rooms = Room.objects.all()
            for _ in range(course.year_level):
                instructor = random.choice(instructors)
                room = random.choice(rooms)
                start_time = random.randint(0, 23)
                end_time = start_time + random.randint(1, 4)
                days_of_week = random.sample(range(7), random.randint(1, 5))
                semester = "First Semester"
                year = 2024
                class_schedule = ClassSchedule(
                    course=course,
                    instructor=instructor,
                    room=room,
                    start_time=start_time,
                    end_time=end_time,
                    days_of_week=days_of_week,
                    semester=semester,
                    year=year,
                )
                schedule.append(class_schedule)
        population.append(schedule)
    return population


def fitness(schedule):
    conflicts = 0
    for class_schedule in schedule:
        conflicts += class_schedule.has_conflict()
    return 1 / (conflicts + 1)


def select_parents(population):
    fitness_values = [fitness(schedule) for schedule in population]
    total_fitness = sum(fitness_values)
    parents = []
    for _ in range(2):
        random_value = random.uniform(0, total_fitness)
        parent_index = 0
        current_fitness = 0
        while current_fitness < random_value:
            parent_index += 1
            current_fitness += fitness_values[parent_index]
        parents.append(population[parent_index])
    return parents


def crossover(parent1, parent2):
    offspring = []
    for course_schedule1, course_schedule2 in zip(parent1, parent2):
        if random.random() < 0.5:
            offspring.append(course_schedule1)
        else:
            offspring.append(course_schedule2)
    return offspring


def mutate(offspring):
    for class_schedule in offspring:
        if random.random() < 0.1:
            class_schedule.instructor = random.choice(
                Instructor.objects.filter(role="Instructor")
            )
            class_schedule.room = random.choice(Room.objects.all())
            class_schedule.start_time = random.randint(0, 23)
            class_schedule.end_time = class_schedule.start_time + random.randint(1, 4)
            class_schedule.days_of_week = random.sample(range(7), random.randint(1, 5))
            class_schedule.semester = "First Semester"
            class_schedule.year = 2024
    return offspring


def run_genetic_algorithm(population_size, generations):
    population = generate_population(population_size)

    for _ in range(generations):
        new_population = []
        for _ in range(population_size):
            parents = select_parents(population)
            offspring = crossover(parents[0], parents[1])
            mutated_offspring = mutate(offspring)
            new_population.append(mutated_offspring)
        population = new_population

    return population
