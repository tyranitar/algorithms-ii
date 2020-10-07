def schedule_jobs(jobs, jobs_len, scorer):
    for i in range(jobs_len):
        job = map(lambda x: float(x), jobs[i].split(' '))
        weight = job[0]
        length = job[1]
        jobs[i] = (weight, length)

    # Breaking ties with larger weight.
    return sorted(jobs, key=lambda x: (scorer(x[0], x[1]), x[0]), reverse=True)

def weighted_completion(jobs, jobs_len):
    completion_time = 0
    ret = 0

    for i in range(jobs_len):
        job = jobs[i]
        weight = job[0]
        length = job[1]
        completion_time += length
        ret += weight * completion_time

    return ret

def main():
    f = open('data/_642c2ce8f3abe387bdff636d708cdb26_jobs.txt')
    jobs = f.readlines()
    jobs_len = int(jobs[0])
    jobs = jobs[1:]
    f.close()

    sorted_by_difference = schedule_jobs(jobs[:], jobs_len, lambda w, l: w - l)
    sorted_by_ratio = schedule_jobs(jobs[:], jobs_len, lambda w, l: w / l)

    difference_weighted_completion = weighted_completion(sorted_by_difference, jobs_len)
    ratio_weighted_completion = weighted_completion(sorted_by_ratio, jobs_len)

    print 'difference: ' + str(int(difference_weighted_completion))
    print 'ratio: ' + str(int(ratio_weighted_completion))

if __name__ == '__main__':
    main()