n, m = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

# n, m = 2, 6
# a = [0, 0, 0, 0, 0, 1]


def decode_answer(question_number, encoded_answer):
    return bool((encoded_answer >> question_number) % 2)

def count_bad_splits(answers):
    counts = []
    section_start = 0
    range_start = 1


    while section_start < len(answers):
        section_end = section_start + 1
        while section_end < len(answers) and answers[section_start] == answers[section_end]:
            section_end += 1

        if section_end == len(answers) and answers[0] == answers[-1] and len(counts) > 0:
            range_start += counts[0]

        counts += reversed(range(range_start, range_start + section_end - section_start))
        section_start = section_end

    if counts[0] == len(answers):
        return len(answers) * [0]

    return counts


total_bad_splits_right = m * [0]
total_bad_splits_left = m * [0]

for question_number in range(n):
    answers = [decode_answer(question_number, encoded_answer) for encoded_answer in a]

    bad_splits_right = count_bad_splits(answers)
    bad_splits_left_tangled = list(reversed(count_bad_splits(list(reversed(answers)))))
    bad_splits_left = [bad_splits_left_tangled[-1]] + bad_splits_left_tangled[:-1]

    total_bad_splits_right = [max(a, b) for a, b in zip(total_bad_splits_right, bad_splits_right)]
    total_bad_splits_left = [max(a, b) for a, b in zip(total_bad_splits_left, bad_splits_left)]


total_bad_splits = sum([min(a + b, m - 1) for a, b in zip(total_bad_splits_left, total_bad_splits_right)]) // 2
good_splits = m * (m - 1) // 2 - total_bad_splits


print(good_splits)
