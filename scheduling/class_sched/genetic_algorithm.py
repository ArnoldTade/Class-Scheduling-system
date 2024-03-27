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


time_slots = {
    "Time": [
        ("07:30", "08:30"),
        ("07:30", "09:00"),
        ("07:30", "09:30"),
        ("07:30", "10:30"),
        ("08:00", "09:00"),
        ("08:00", "09:30"),
        ("08:00", "10:00"),
        ("08:00", "11:00"),
        ("08:30", "9:30"),
        ("08:30", "10:00"),
        ("08:30", "10:30"),
        ("08:30", "11:30"),
        ("09:00", "10:00"),
        ("09:00", "10:30"),
        ("09:00", "11:00"),
        ("09:00", "12:00"),
        ("09:30", "10:30"),
        ("09:30", "11:00"),
        ("09:30", "11:30"),
        ("10:00", "11:00"),
        ("10:00", "11:30"),
        ("10:00", "12:00"),
        ("10:30", "11:30"),
        ("10:30", "12:00"),
        ("11:00", "12:00"),
        #### NOON ####
        ("13:00", "14:00"),
        ("13:00", "14:30"),
        ("13:00", "15:00"),
        ("13:00", "16:00"),
        ("13:30", "14:30"),
        ("13:30", "15:00"),
        ("13:30", "15:30"),
        ("13:30", "16:30"),
        ("14:00", "15:00"),
        ("14:00", "15:30"),
        ("14:00", "16:00"),
        ("14:00", "17:00"),
        ("14:30", "15:30"),
        ("14:30", "16:00"),
        ("14:30", "16:30"),
        ("14:30", "17:30"),
        ("15:00", "16:00"),
        ("15:00", "16:30"),
        ("15:00", "17:00"),
        ("15:00", "18:00"),
        ("15:30", "16:30"),
        ("15:30", "17:00"),
        ("15:30", "17:30"),
        ("15:30", "18:30"),
        ("16:00", "17:00"),
        ("16:00", "17:30"),
        ("16:00", "18:00"),
        ("16:00", "19:00"),
        ("16:30", "17:30"),
        ("16:30", "18:00"),
        ("16:30", "18:30"),
        ("16:30", "19:30"),
        ("17:00", "18:00"),
        ("17:00", "18:30"),
        ("17:00", "19:00"),
        ("17:00", "20:00"),
        ("17:30", "18:30"),
        ("17:30", "19:00"),
        ("17:30", "19:30"),
        ("17:30", "20:00"),
        ("18:00", "19:00"),
        ("18:00", "19:30"),
        ("18:00", "20:00"),
        ("18:30", "19:30"),
        ("18:30", "20:00"),
        ("19:00", "20:00"),
    ],
}
days_of_week = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "M",
    "T",
    "W",
    "TH",
    "F",
    "S",
    "M-W-F",
    "T-TH",
    "W-F",
    "TH-F",
    "M-W",
]
for day in days_of_week:
    time_slots[day] = time_slots["Time"]


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
                    fitness -= 5
                    print(
                        f"Conflict: Instructor {instructor.lastName} assigned to both classes at the same time in room {room.room_name}."
                    )
                break

            # Check for room type mismatch (optional)
            if room.room_type == "Lecture" and class_schedule.course.type in [
                "Lab",
                "Lab and Lec",
            ]:
                fitness -= 1

            ######### TIME AVALABILITY #########
            start_time = datetime.strptime(class_schedule.start_time, "%H:%M").time()
            end_time = datetime.strptime(class_schedule.end_time, "%H:%M").time()
            class_duration = (end_time.hour - start_time.hour) + (
                end_time.minute - start_time.minute
            ) / 60

            if instructor.status == "Permanent" or instructor.status == "Temporary":
                start_time = datetime.strptime(
                    class_schedule.start_time, "%H:%M"
                ).time()
                end_time = datetime.strptime(class_schedule.end_time, "%H:%M").time()

                if start_time.hour >= 17 and end_time.hour >= 17:
                    fitness -= 2
                    # print(start_time.hour, end_time.hour)
                    print(
                        f"Permanent instructor {instructor.lastName} has a class exceeding 5:00 PM: {start_time} - {end_time}"
                    )

                else:
                    print(
                        f"Permanent instructor {instructor.lastName} has a valid class: {start_time} - {end_time}"
                    )

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

        ### ROOM ###
        lecture_rooms = Room.objects.filter(
            college=class_schedule.instructor.college, room_type="Lecture"
        )
        lab_rooms = Room.objects.filter(
            college=class_schedule.instructor.college, room_type="Lab and Lecture"
        )
        if class_schedule.course.type == "Lec":
            available_rooms = lecture_rooms
        elif class_schedule.course.type == "Lec and Lab":
            available_rooms = lab_rooms
        else:
            available_rooms = []
        # print(available_rooms)

        if available_rooms:
            class_schedule.room = random.choice(available_rooms)

        ### TIME ###
        mutation_probability = 0.3
        if random.random() < mutation_probability:
            hours = class_schedule.course.hours
            weekday_ranges = {
                1: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
                2: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
                3: [
                    "M-W-F",
                    "T-TH",
                    # "Saturday",
                    "M-W-F",
                    "T-TH",
                    "M-W",
                    "M-W-F",
                    "W-F",
                    "T-TH",
                ],
                4: ["M-W", "W-F", "T-TH"],
                5: ["M-W-F", "T-TH"],
                6: ["M-W-F", "T-TH", "TH-F"],
            }
            days_of_week = random.choice(weekday_ranges[hours])
            if "-" in days_of_week:
                num_sessions = len(days_of_week.split("-"))
            else:
                num_sessions = 1
            session_duration_hours = class_schedule.course.hours / num_sessions
            session_duration_minutes = int(round(session_duration_hours * 60))

            chosen_weekdays = (
                random.sample(days_of_week.split("-"), 1)[0]
                if "-" in days_of_week
                else days_of_week
            )

            found_valid_slot = False
            if (
                class_schedule.instructor.status == "Permanent"
                or class_schedule.instructor.status == "Temporary"
            ):
                filtered_time_slots = [
                    slot
                    for slot in time_slots[chosen_weekdays]
                    if datetime.strptime(slot[1], "%H:%M").hour < 17
                ]
                start_index = random.randint(0, len(filtered_time_slots) - 1)
                for j in range(start_index, len(filtered_time_slots)):
                    start_time, end_time = filtered_time_slots[j]

                    slot_duration_in_minutes = (
                        datetime.strptime(end_time, "%H:%M")
                        - datetime.strptime(start_time, "%H:%M")
                    ).total_seconds() / 60

                    if slot_duration_in_minutes == session_duration_minutes:
                        valid_time_slots = [(start_time, end_time)]
                        found_valid_slot = True
                        break

                class_schedule.days_of_week = days_of_week
                class_schedule.start_time = start_time
                class_schedule.end_time = end_time
                print("Final Schedule: ", days_of_week, start_time, end_time)
            else:
                filtered_time_slots = time_slots[chosen_weekdays]
                start_index = random.randint(0, len(filtered_time_slots) - 1)
                for j in range(start_index, len(filtered_time_slots)):
                    start_time, end_time = filtered_time_slots[j]

                    slot_duration_in_minutes = (
                        datetime.strptime(end_time, "%H:%M")
                        - datetime.strptime(start_time, "%H:%M")
                    ).total_seconds() / 60

                    if slot_duration_in_minutes == session_duration_minutes:
                        valid_time_slots = [(start_time, end_time)]
                        found_valid_slot = True
                        break

                class_schedule.days_of_week = days_of_week
                class_schedule.start_time = start_time
                class_schedule.end_time = end_time
                print("Final Schedule: ", days_of_week, start_time, end_time)

        class_schedule.save()
        self.fitness = self.calculate_fitness()

        # self.other_time_slot = self.select_other_timeslot(valid_time_slots)


def generate_population(population_size, valcollege, valschool_year, valsemester):
    population = []
    for i in range(population_size):
        class_schedules = []
        for instructor_course in InstructorCourse.objects.filter(
            instructor__college=valcollege
        ):
            instructor = instructor_course.instructor
            course = instructor_course.course
            section = instructor_course.section.program_section

            #### ROOMS ####
            lecture_rooms = Room.objects.filter(
                college=instructor.college, room_type="Lecture"
            )
            lab_rooms = Room.objects.filter(
                college=instructor.college, room_type="Lab and Lecture"
            )

            if course.type == "Lec":
                available_rooms = lecture_rooms
            elif course.type == "Lab and Lec":
                available_rooms = lab_rooms
            else:
                available_rooms = []

            room = None
            if available_rooms:
                room = random.choice(available_rooms)
            if not room:
                print("No available rooms for: ", instructor_course)
                continue

            #### CHOOSE DAY ####
            hours = instructor_course.course.hours
            weekday_ranges = {
                1: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
                2: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
                3: [
                    "M-W-F",
                    "T-TH",
                    # "Saturday",
                    "M-W-F",
                    "T-TH",
                    "M-W",
                    "M-W-F",
                    "W-F",
                    "T-TH",
                ],
                4: ["M-W", "W-F", "T-TH"],
                5: ["M-W-F", "T-TH"],
                6: ["M-W-F", "T-TH", "TH-F"],
            }
            days_of_week = random.choice(weekday_ranges[hours])
            if "-" in days_of_week:
                num_sessions = len(days_of_week.split("-"))
            else:
                num_sessions = 1

            session_duration_hours = hours / num_sessions
            session_duration_minutes = int(round(session_duration_hours * 60))

            chosen_weekdays = (
                random.sample(days_of_week.split("-"), 1)[0]
                if "-" in days_of_week
                else days_of_week
            )

            found_valid_slot = False
            start_index = random.randint(0, len(time_slots[chosen_weekdays]) - 1)
            for j in range(start_index, len(time_slots[chosen_weekdays])):
                start_time, end_time = time_slots[chosen_weekdays][j]

                slot_duration_in_minutes = (
                    datetime.strptime(end_time, "%H:%M")
                    - datetime.strptime(start_time, "%H:%M")
                ).total_seconds() / 60

                if slot_duration_in_minutes == session_duration_minutes:
                    valid_time_slots = [(start_time, end_time)]
                    found_valid_slot = True
                    # print("Valid time slots for: ", instructor_course, valid_time_slots)

                    break
            if not found_valid_slot:
                # print("No valid time slots for: ", instructor_course)
                continue

            start_time, end_time = random.choice(valid_time_slots)
            class_schedule = ClassSchedule(
                course=course,
                instructor=instructor,
                section=section,
                room=room,
                start_time=start_time,
                end_time=end_time,
                days_of_week=days_of_week,
                semester=valsemester,
                year=valschool_year,
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
