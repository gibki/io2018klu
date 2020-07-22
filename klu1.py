n, m = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]


def decode_answer(question_number, encoded_answer):
    return bool((encoded_answer >> question_number) % 2)

def group_view(question, encoded_group_views):
    has_yes = False
    has_no = False
    for encoded_member_view in encoded_group_views:
        if decode_answer(question, encoded_member_view):
            has_yes = True
        else:
            has_no = True

        if has_yes and has_no:
            return 'MIXED'

    if has_yes:
        return 'YES'
    return 'NO'


def generate_splits(members):
    for first_split in range(members):
        for second_split in range(first_split + 1, members):

            first_group = [x % members for x in range(first_split, second_split)]
            second_group = [x % members for x in range(second_split, first_split + members)]

            yield first_group, second_group


number_of_splits = 0

for first_group, second_group in generate_splits(m):
    first_group_encoded_views = [a[i] for i in first_group]
    second_group_encoded_views = [a[i] for i in second_group]

    all_questions_valid = True
    for question in range(n):
        all_questions_valid = all_questions_valid and \
            group_view(question, first_group_encoded_views) == group_view(question, second_group_encoded_views)

    if all_questions_valid:
        number_of_splits += 1

print(number_of_splits)
