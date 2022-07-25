# функция для 1 и 3 теста тк 2 тест считаю неправильным
def appearance(intervals):
    timestamps = []

    for category in intervals:
        for i, timestamp in enumerate(intervals[category]):
            timestamps.append((timestamp, i % 2))

    timestamps.sort()
    at_the_same_time = 0
    buff_timestamp = 0
    answ = 0

    for timestamp in timestamps:
        if timestamp[1] == 0:
            at_the_same_time += 1
        else:
            at_the_same_time -= 1
        if at_the_same_time == 3:
            buff_timestamp = timestamp[0]
        elif buff_timestamp != 0 and at_the_same_time < 3:
            answ += timestamp[0] - buff_timestamp
            buff_timestamp = 0
    return answ


# (костыль) рефактор когда с другой сессии пользователь зашел, но не вышел из другой
def refactor(array):
    refactored_array = array[0:2]
    buf_end = array[1][0]

    for i in range(2, len(array), 2):
        if array[i][0] > buf_end:
            refactored_array += array[i:i + 2]

            buf_end = array[i + 1][0]
        elif array[i + 1][0] > buf_end:
            buf_end = array[i + 1][0]
            refactored_array.pop()
            refactored_array.append(array[i + 1])
    return refactored_array


# функция с костылем
def appearance2(intervals):
    less = []
    pupil = []
    tutor = []
    for category in intervals:
        for i, timestamp in enumerate(intervals[category]):

            if category == 'lesson':
                less.append((timestamp, i % 2))
            elif category == 'pupil':
                pupil.append((timestamp, i % 2))
            else:
                tutor.append((timestamp, i % 2))
    less, pupil, tutor = refactor(less), refactor(pupil), refactor(tutor)
    timestamps = sorted(less + pupil + tutor)
    at_the_same_time = 0
    buff_timestamp = 0
    answ = 0
    for timestamp in timestamps:
        if timestamp[1] == 0:
            at_the_same_time += 1
        else:
            at_the_same_time -= 1
        if at_the_same_time == 3:
            buff_timestamp = timestamp[0]
        elif buff_timestamp != 0 and at_the_same_time < 3:
            answ += timestamp[0] - buff_timestamp
            buff_timestamp = 0
    return answ


tests = [

    {
        'data': {
            'lesson': [1594663200, 1594666800],
            'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
            'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},

        'answer': 3117
    },

    {
        'data': {
            'lesson': [1594702800, 1594706400],
            'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150,
                      1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480,
                      1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503,
                      1594706524, 1594706524, 1594706579, 1594706641],
            'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},

        'answer': 3577

    },

    {
        'data': {
            'lesson': [1594692000, 1594695600],
            'pupil': [1594692033, 1594696347],
            'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},

        'answer': 3565

    },

]

if __name__ == '__main__':

    for i, test in enumerate(tests):
        test_answer = appearance2(test['data'])

        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
