import random

# Import your Django models
from class_sched.models import Instructor, Room, Course, ClassSchedule
from .models import *
from datetime import datetime, date, timedelta


instructors = InstructorCourse.objects.values_list("instructor", flat=True)
courses = InstructorCourse.objects.values_list("course", flat=True)
sections = InstructorCourse.objects.values_list("section", flat=True)
rooms = Room.objects.all()
weeks = Week.objects.all()


class Individual:
    def __init__(self, class_schedules):
        self.class_schedules = class_schedules
        self.fitness = self.calculate_fitness()

    def calculate_fitness(self):
        fitness = 0
        for class_schedule in self.class_schedules:
            instructor = class_schedule.instructor
            room = class_schedule.room
            for other_class_schedule in self.class_schedules:
                if class_schedule == other_class_schedule:
                    continue
                # Check for instructor and room conflicts
                if (
                    instructor == other_class_schedule.instructor
                    and room == other_class_schedule.room
                    and class_schedule.days_of_week == other_class_schedule.days_of_week
                    and self.check_time_overlap(
                        class_schedule.start_time,
                        class_schedule.end_time,
                        other_class_schedule.start_time,
                        other_class_schedule.end_time,
                    )
                ):
                    fitness -= 1
                    break
            # Check instructor availability based on status (optional)
            if instructor.status == "Full time" and (
                datetime.strptime(class_schedule.start_time, "%H:%M")
                < datetime.strptime("08:00", "%H:%M")
                or datetime.strptime(class_schedule.end_time, "%H:%M")
                > datetime.strptime("17:00", "%H:%M")
            ):
                fitness -= 1
            elif instructor.status == "Part time" and (
                datetime.strptime(class_schedule.start_time, "%H:%M")
                < datetime.strptime("17:00", "%H:%M")
                or datetime.strptime(class_schedule.end_time, "%H:%M")
                > datetime.strptime("20:00", "%H:%M")
            ):
                fitness -= 1
            # Check for time constraints (optional)
            if (
                datetime.strptime(class_schedule.start_time, "%H:%M")
                < datetime.strptime("08:00", "%H:%M")
                or datetime.strptime(class_schedule.end_time, "%H:%M")
                > datetime.strptime("12:00", "%H:%M")
                or (
                    datetime.strptime(class_schedule.start_time, "%H:%M")
                    >= datetime.strptime("13:00", "%H:%M")
                    and datetime.strptime(class_schedule.end_time, "%H:%M")
                    > datetime.strptime("17:00", "%H:%M")
                )
            ):
                fitness -= 1
            # Check for room type mismatch (optional)
            if room.room_type == "Lecture" and class_schedule.course.type in [
                "Lab",
                "Lab and Lec",
            ]:
                fitness -= 1
        return fitness

    @staticmethod
    def check_time_overlap(start1, end1, start2, end2):
        start1_time = datetime.strptime(start1, "%H:%M")
        end1_time = datetime.strptime(end1, "%H:%M")
        start2_time = datetime.strptime(start2, "%H:%M")
        end2_time = datetime.strptime(end2, "%H:%M")
        return (start1_time <= end2_time) and (start2_time <= end1_time)

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
        class_schedule_index = random.randint(0, len(self.class_schedules) - 1)
        try:
            class_schedule = self.class_schedules[class_schedule_index]
        except IndexError:
            print(f"IndexError in mutate: {class_schedule_index}")
            return

        # Modify only room, start_time, and end_time
        class_schedule.room = random.choice(
            [room for room in Room.objects.all() if room != class_schedule.room]
        )
        """
        hour = random.choice([8, 9, 10, 11, 13, 14, 15])
        minute = random.choice([0, 30])
        start_time = f"{hour}:{minute:02d}"
        end_hour = hour + 3 if minute == 30 else hour + 2
        if end_hour == 12:
            end_hour += 1
        end_time = f"{end_hour}:{minute:02d}"
        class_schedule.start_time = start_time
        class_schedule.end_time = end_time"""

        class_schedule.save()

        self.fitness = self.calculate_fitness()


def generate_population(population_size, schedule_length=150):
    population = []
    for i in range(population_size):
        class_schedules = []
        for instructor_course in InstructorCourse.objects.all():
            instructor = instructor_course.instructor
            course = instructor_course.course
            section = instructor_course.section.program_section

            # ROOMS
            available_rooms = Room.objects.filter(
                college=instructor.college, room_type__in=[course.type, "Lecture"]
            )
            if not available_rooms:
                continue

            room = random.choice(available_rooms)

            # CHOOSE DAY
            hours = instructor_course.course.hours
            days_of_week = None
            session_duration_hours = 0
            session_duration_minutes = 0

            weekday_ranges = {
                2: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
                3: ["M-W-F", "T-TH", "Saturday"],
                4: ["M-W", "W-F", "T-TH"],
                5: ["M-W-F", "T-TH"],
                6: ["M-W-F", "T-TH", "TH-F"],
            }
            if hours in weekday_ranges:
                days_of_week = random.choice(weekday_ranges[hours])
                days_of_week = random.choice(weekday_ranges[hours])
                num_sessions = len(days_of_week.split("-"))
                session_duration_hours = hours / num_sessions
                session_duration_minutes = (
                    session_duration_hours - int(session_duration_hours)
                ) * 60
            else:
                days_of_week = random.choice(
                    ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
                )

            max_start_hour = 16
            if session_duration_hours == 3:
                max_start_hour -= 2  # Avoid exceeding 5 PM for 3-hour sessions
            elif session_duration_minutes == 30:
                max_start_hour -= 1

            # TIME
            hour = random.choice([8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20])
            minute = random.choice([0, 30])

            start_time = f"{hour}:{minute:02d}"
            start_time_datetime = datetime.strptime(start_time, "%H:%M")

            end_time_datetime = start_time_datetime + timedelta(
                hours=int(session_duration_hours), minutes=int(session_duration_minutes)
            )

            end_time = end_time_datetime.strftime("%H:%M")
            """
            if end_hour == 12:
                end_hour += 1
                end_time = f"{end_hour}:{minute:02d}"
            else:
                end_time = f"{end_hour}:{minute:02d}"""

            # SEMESTER AND YEAR
            semester = "Second Semester"
            year = "2024 - 2025"

            class_schedule = ClassSchedule(
                course=course,
                instructor=instructor,
                section=section,
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
    parent = max(population, key=lambda individual: individual.fitness)
    return parent


def evolve(population, num_generations):
    for generation in range(num_generations):
        parent1 = select_parent(population)
        parent2 = select_parent(population)

        child1 = Individual.crossover(parent1, parent2)
        child2 = Individual.crossover(parent1, parent2)

        child1.mutate()
        child2.mutate()

        population.append(child1)
        population.append(child2)

        population.sort(key=lambda individual: individual.fitness, reverse=True)
        population.pop()
        population.pop()

    return max(population, key=lambda individual: individual.fitness)
