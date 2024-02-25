import random
from collections import defaultdict

# Import your Django models
from class_sched.models import Instructor, Room, Course, ClassSchedule, Conflict
from .models import ClassSchedule
from datetime import datetime, date, timedelta


class Individual:
    def __init__(self, class_schedules):
        self.class_schedules = class_schedules
        self.fitness = self.calculate_fitness()

    def calculate_fitness(self):
        fitness = 0
        for class_schedule in self.class_schedules:
            instructor = class_schedule.instructor
            room = class_schedule.room
            if instructor.status == "Full time" and (
                class_schedule.start_time < "08:00" or class_schedule.end_time > "17:00"
            ):
                fitness -= 1
            elif instructor.status == "Part time" and (
                class_schedule.start_time < "17:00" or class_schedule.end_time > "20:00"
            ):
                fitness -= 1
            if (
                class_schedule.start_time < "08:00"
                or class_schedule.end_time > "12:00"
                or (
                    class_schedule.start_time >= "13:00"
                    and class_schedule.end_time > "17:00"
                )
            ):
                fitness -= 1
            if room.room_type == "Lecture" and class_schedule.course.type in [
                "Lab",
                "Lab and Lecture",
            ]:
                fitness -= 1
            conflicts = Conflict.objects.filter(
                schedule__instructor=instructor,
                schedule__room=room,
                schedule__days_of_week=class_schedule.days_of_week,
                schedule__semester=class_schedule.semester,
                schedule__year=class_schedule.year,
            )
            if conflicts:
                fitness -= len(conflicts)
        return fitness

    @staticmethod
    def crossover(parent1, parent2):
        child = Individual([])

        child_class_schedules = []
        num_class_schedules = min(
            len(parent1.class_schedules), len(parent2.class_schedules)
        )
        for i in range(num_class_schedules):
            class_schedule_index = random.randint(0, len(parent1.class_schedules) - 1)
            child_class_schedules.append(parent1.class_schedules[class_schedule_index])
        for class_schedule in parent2.class_schedules:
            if class_schedule not in child_class_schedules:
                child_class_schedules.append(class_schedule)
        child.class_schedules = child_class_schedules
        child.fitness = child.calculate_fitness()
        return child

    def mutate(self):
        # Choose a random class schedule to mutate
        class_schedule_index = random.randint(0, len(self.class_schedules))

        # Randomly modify the class schedule
        class_schedule = self.class_schedules[class_schedule_index]
        class_schedule.instructor = random.choice(
            [
                instructor
                for instructor in Instructor.objects.all()
                if instructor != class_schedule.instructor
            ]
        )
        class_schedule.room = random.choice(
            [room for room in Room.objects.all() if room != class_schedule.room]
        )
        class_schedule.save()
        self.fitness = self.calculate_fitness()


def generate_population(population_size):
    population = []
    for i in range(population_size):
        class_schedules = []
        for course in Course.objects.all():
            available_instructors = Instructor.objects.filter(
                status="Full time"
            ) | Instructor.objects.filter(status="Part time", college=course.college)
            if not available_instructors:
                continue
            instructor = random.choice(available_instructors)
            available_rooms = Room.objects.filter(
                college=instructor.college, room_type__in=[course.type, "Lecture"]
            )
            if not available_rooms:
                continue
            room = random.choice(available_rooms)
            hour = random.choice([8, 9, 10, 11, 13, 14, 15])
            minute = random.choice([0, 30])

            start_time = f"{hour}:{minute:02d}"
            end_hour = hour + 3 if minute == 30 else hour + 2
            end_time = f"{end_hour}:{minute:02d}"

            days_of_week = random.choice(
                ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
            )
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
            class_schedules.append(class_schedule)
        # Ensure that each Individual has at least one ClassSchedule
        if not class_schedules:
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
            class_schedules.append(class_schedule)
        individual = Individual(class_schedules)
        population.append(individual)
    return population


def select_parent(population):
    # Select the parent with the highest fitness score
    parent = max(population, key=lambda individual: individual.fitness)
    return parent


def evolve(population, num_generations):
    # Evolve the population over multiple generations
    for generation in range(num_generations):
        # Select two parent individuals
        parent1 = select_parent(population)
        parent2 = select_parent(population)

        # Create one or more child individuals using crossover
        child1 = Individual.crossover(parent1, parent2)
        child2 = Individual.crossover(parent1, parent2)

        # Mutate the child individuals
        child1.mutate()
        child2.mutate()

        # Add the child individuals to the population
        population.append(child1)
        population.append(child2)

        # Remove the two worst-performing individuals from the population
        population.sort(key=lambda individual: individual.fitness, reverse=True)
        population.pop()
        population.pop()

    # Return the best-performing individual
    return max(population, key=lambda individual: individual.fitness)
