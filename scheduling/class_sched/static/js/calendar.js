document.addEventListener('DOMContentLoaded', function () {
    var calendarEl = document.getElementById('calendarSchedulePage');

    var calendar = new FullCalendar.Calendar(calendarEl, {
        timeZone: 'UTC',
        initialView: 'timeGridWeek',
        headerToolbar: {
            right: 'timeGridWeek,timeGridDay'
        },
        dayHeaderFormat: { weekday: 'short' },
        events: eventSchedules
    });

    calendar.render();
});
