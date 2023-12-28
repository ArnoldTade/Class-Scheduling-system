
document.addEventListener('DOMContentLoaded', function () {
    var calendarEl = document.getElementById('calendar');

    var calendar = new FullCalendar.Calendar(calendarEl, {
        timeZone: 'UTC',
        initialView: 'dayGridWeek',
        headerToolbar: {
            left: 'prev,next',
            center: 'title',
            right: 'dayGridWeek,dayGridDay'
        },
        editable: true,
        events: '/api/demo-feeds/events.json'
    });

    calendar.render();
});
