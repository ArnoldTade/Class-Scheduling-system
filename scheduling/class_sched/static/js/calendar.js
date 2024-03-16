document.addEventListener('DOMContentLoaded', function () {
    var calendarEl = document.getElementById('calendarSchedulePage');

    var calendar = new FullCalendar.Calendar(calendarEl, {
        timeZone: 'UTC',
        initialView: 'timeGridWeek',
        headerToolbar: {
            right: 'timeGridWeek,timeGridDay'
        },
        dayHeaderFormat: { weekday: 'short' },
        slotMinTime: '07:00:00',
        slotMaxTime: '21:00:00',
        events: eventSchedules,

    });

    calendar.render();
});
