#0是人 1是狼 2是羊 3是菜 人永远在船上
name = ['‍农夫','狼','羊','菜']
cnt = 0
def safe_status(status):
    if status[1] == status[2]:
        if status[0]!= status[2]:
            return False
    if status[2] == status[3]:
        if status[0] != status[2]:
            return False
    return True

def all_crossed(status):
    return status[0] and status[1] and status[2] and status[3]

def create_sit_of_nextstatus(status):
    all_next_status = []
    for i in range(0, 4):
        if status[0] == status[i]:
            next_status = [status[0], status[1], status[2], status[3]]
            next_status[0] = not next_status[0]
            # farmer acrossed
            next_status[i] = next_status[0]
            # sth along with farmer
            if safe_status(next_status):
                all_next_status.append(next_status)
    return all_next_status

def show(status,riverside):
    result=""
    for i in range(0,4):
        if status[i]==riverside:
            if len(result)!=0:
                result+=","
            result+=name[i]
    return result

def print_all_history(all_history_status):
    for status in all_history_status:
        print(show(status,False)+"->"+show(status,True))

def search_step(all_history_status):
    global cnt
    current_status = all_history_status[len(all_history_status) - 1]
    # the last part of history status
    all_next_status = create_sit_of_nextstatus(current_status)
    for next_status in all_next_status:
        if next_status in all_history_status:
            continue
        # repeated
        all_history_status.append(next_status)
        if all_crossed(next_status):
            cnt += 1
            print("way" + str(cnt) + ":")
            print_all_history(all_history_status)
        else:
            search_step(all_history_status)
        all_history_status.pop()

status = [False,False,False,False]
all_history_status=[status]
search_step(all_history_status)