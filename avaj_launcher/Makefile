MAIN_CLASS = src.Simulator
BUILD_DIR = build

build:
# create the build dir to store the .class files
	@mkdir -p ${BUILD_DIR}

#recursively find the paths for the .java file starting from root and redirect to .txt
	@find * -name "*.java" > sources.txt

#converts the .javas to bytecode and -d specifies where to store the .class files
	@javac -d ${BUILD_DIR} @sources.txt

run:
#run the code, -cp tells where to look for the .class
	@java -cp ${BUILD_DIR} ${MAIN_CLASS} scenario.txt

all: build run

clean:
	@rm -rf ${BUILD_DIR}
	@rm -rf sources.txt

re: clean all


#error files test
empty: clean build
	@java -cp ${BUILD_DIR} ${MAIN_CLASS} ./error_testfiles/empty.txt

iter: clean build
	@java -cp ${BUILD_DIR} ${MAIN_CLASS} ./error_testfiles/invalid_iter.txt

line1: clean build
	@java -cp ${BUILD_DIR} ${MAIN_CLASS} ./error_testfiles/invalid_line1.txt

line2: clean build
	@java -cp ${BUILD_DIR} ${MAIN_CLASS} ./error_testfiles/invalid_line2.txt

line3: clean build
	@java -cp ${BUILD_DIR} ${MAIN_CLASS} ./error_testfiles/invalid_line3.txt

nocraft: clean build
	@java -cp ${BUILD_DIR} ${MAIN_CLASS} ./error_testfiles/no_aircraft.txt

nofile: clean build
	@java -cp ${BUILD_DIR} ${MAIN_CLASS} I_AM_UR_MOM.txt

