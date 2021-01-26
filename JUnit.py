
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