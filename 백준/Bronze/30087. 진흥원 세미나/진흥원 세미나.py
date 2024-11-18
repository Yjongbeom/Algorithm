seminar_dict = { "Algorithm": "204", "DataAnalysis": "207", "ArtificialIntelligence": "302", "CyberSecurity": "B101", "Network": "303", "Startup": "501", "TestStrategy": "105" }
N = int(input())

seminars = [input() for _ in range(N)]

for seminar in seminars:
    print(seminar_dict[seminar])