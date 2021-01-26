def getGrade(mid, ct, finalExam, attendance):
	total = mid+ct+finalExam+attendance
	grade = ""
	if(total >= 80):
		grade = "A+"
	if(total >=70):
		grade = "A";
	if (total >= 60):
		grade = "B"
	if (total >= 50):
		grade = "C"
	if (total <= 50):
		grade = "F"

	return grade;

def generateJavaFiles():
    filepath = 'worst.csv'
    javaFile = 'getGradeUnitTesting_worst.java'

    with open(filepath) as file:
        wf = open(javaFile,'w')
        line= file.readline()

        while line:
            line = file.readline()

            values = line.strip().split(',')
            if(len(values) == 0):
                break
            wf.write('@Test\npublic void getGrade_worstCase_#' + values[0] + '(){\n\tGradeCalculator gradeCalculator = ne'
                                                                       'w GradeCalculator();\n\tString grade = gradeCalculator.getGrade'
                                                                       '('+values[1]+', '+values[2]+', '+values[3]+', '+values[4]+');'
                                                                        '\n\tString expected = \'E\';\n\t'
                                                                        'assertEquals(expected,grade);\n}\n\n')


            if(line == ''):
                break

def generateReportFiles():
    filepath = 'worst.csv'
    reportFile = 'getGradeReport_worst.csv'

    with open(filepath) as file:
        wf = open(reportFile,'w')
        line= file.readline()
        values = line.strip().split(',')
        values.append('Actual Output')
        values.append('Comment')

        for val in range(0,len(values)-1):
            wf.write(values[val])
            wf.write(',')
        wf.write(values[len(values)-1]+'\n')

        while line:
            line = file.readline()
            values = line.strip().split(',')
            values.pop(len(values)-1)
            values.append('E')
            values.append(str(getGrade(int(values[1]),int(values[2]),int(values[3]),int(values[4]))))
            values.append('failed')

            for val in range(0, len(values) - 1):
                wf.write(values[val]+',')
            wf.write(values[len(values) - 1] + '\n')

            if(line == ''):
                break