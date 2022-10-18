const lessons = []

lessons.push({
    title: 'Pause',
    startTime: '12:00',
    endTime: '12:30',
    daysOfWeek: [1,2,3,4,5],
    startRecur: Date('2022-09-13'),
    endRecur: Date('2023-07-28'),
})

const fill_lesons = () => {
    json_lessons.forEach(lesson => {
        lessons.push({
            id: lesson.subject,
            title: `${lesson.subject}(${lesson.teacher})`,
            startTime: lesson.timefrom,
            endTime: lesson.timeto,
            daysOfWeek: [lesson.day],
            startRecur: Date('2022-09-13'),
            endRecur: Date('2023-07-28')
        })
    });
}

fill_lesons()

const calendarEl = document.getElementById('timetable');
const calendar = new FullCalendar.Calendar(calendarEl, {
    initialView: 'timeGridWeek',

    headerToolbar: {
        center: 'timeGridWeek,timeGridDay'
    },

    events: lessons
});
calendar.render();