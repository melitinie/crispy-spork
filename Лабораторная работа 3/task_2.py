def find_common_participants(participants_first_group, participants_second_group, s=','):
    intersection_set = set(participants_first_group.split(s)).intersection(set(participants_second_group.split(s)))
    return sorted(list(intersection_set))


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

find_common_participants(participants_first_group, participants_second_group, s='|')