from classes.process import Process
from classes.regiao_critica import CriticalSection
from random import randint, shuffle


if __name__ == '__main__':
    results = open("files/results.txt", "w")

    for q in range(200):
        # creates processes and sorts randomly
        processes_queue = [Process(
            F"Process {i + 1}", i, [randint(1, 100) for _ in range(10)]) for i in range(10)
        ]
        shuffle(processes_queue)

        # updating from critical section
        section = CriticalSection()

        for process in processes_queue:
            if process.pid < 5:
                try:
                    for value in process.array:
                        section.vetor_add(value)
                        print(
                            F"{process.name} added {value} at position {len(section.vector)}",
                            file=results
                        )
                except IndexError as e:
                    print(F"Could not add: {e.args}", file=results)
            else:
                for _ in range(len(process.array)):
                    try:
                        print(
                            F"Process {process.name} removed the value {section.vector[-1]}",
                            file=results
                        )
                        section.vetor_rem()
                    except IndexError as e:
                        print(F"{process.name} could not remove: {e}", file=results)

        # show queue elements
        if section.vector:
            print(F"\nCritical section elements: {section.vector}", file=results)
            print(F"Total: {len(section.vector)} elements", file=results)
        else:
            print("Critical section is empty!", file=results)
    print("\n>> The result will be available in results.txt in files directory.\n")
    exit()
