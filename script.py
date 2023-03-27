def calculate_study_time(N, M, topics):
    # use a dictionary as data structure
    # each key value pair will have the following structure
    # {i: (Ji, Ti)}
    study_time = {}
    
    # for each topic, calculate J (how long it takes to study each question in topic i)
    for i in range(M):
        Ki, Ti = topics[i][0], topics[i][1]
        # store Ji and Ti in dictionary at index i
        study_time[i] = [Ki/Ti, Ti]

    # sort the dictionary by J increasing
    # the programmer will first want to study the topics where J is smaller
    study_time = dict(sorted(study_time.items(), key=lambda item: item[1][0]))

    # calculate how long to spend on each topic
    for j in study_time:

        # if there are no more hours left, dedicate 0 hours to topic j
        if N < 0:
            study_time[j].append(0)
            continue
        
        # decrement N by how long it will take to cover topic j
        Ti = study_time[j][1]
        N -= Ti

        # if there are enough hours left to study this whole topic
        # append the number of hours to the dictionary
        if N >= 0:
            study_time[j].append(Ti)
        # otherwise, append the remaining hours
        else:
            study_time[j].append(Ti + N)

    return study_time

if __name__ == '__main__':
    # parse input
    N, M, L = map(int, input().split())
    topics = []
    for i in range(M):
            Ki, Ti = map(int, input().split())
            topics.append([Ki, Ti])

    # calculate how many hours to dedicate to each topic
    study_time = calculate_study_time(N, M, topics)

    # construct output string
    output = "The programmer will have to spend"
    for j in study_time:
        output += f" {study_time[j][2]} hour(s) on topic {j},"

    print(output[:-1] + ".")