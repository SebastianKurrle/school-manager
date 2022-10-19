
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
            groupId: lesson.subject,
            startRecur: Date('2022-09-13'),
            endRecur: Date('2023-07-28'),
            title: `${lesson.subject}(${lesson.teacher})`,
            startTime: lesson.timefrom,
            endTime: lesson.timeto,
            daysOfWeek: [lesson.day],
        })
    });
}

fill_lesons()

let timetableEl = document.getElementById('timetable');
let timetable = new FullCalendar.Calendar(timetableEl, {
    initialView: 'timeGridWeek',

    headerToolbar: {
        center: 'timeGridWeek,timeGridDay'
    },

    events: lessons
});

timetable.render()
