MAIN_CLASS = src.Simulator
BUILD_DIR = build

all:

# create the build dir to store the .class files
	@mkdir -p ${BUILD_DIR}

#recursively find the paths for the .java file starting from root and redirect to .txt
	@find * -name "*.java" > sources.txt

#converts the .javas to bytecode and -d specifies where to store the .class files
	@javac -d ${BUILD_DIR} @sources.txt

#run the code, -cp tells where to look for the .class
	@java -cp ${BUILD_DIR} ${MAIN_CLASS} scenario.txt

clean:
	@rm -rf ${BUILD_DIR}
	@rm -rf sources.txt

re: clean all

