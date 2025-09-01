
all: 
	@echo "사용법: make [파일명]"

%: %.o
	g++ -o $@ $<

%.o: %.cpp
	g++ -c -o $@ $<

clean:
	@find . -maxdepth 1 -type f ! -name '*.cpp' ! -name 'Makefile' -exec rm -f {} +
	@echo "Cleaned up files."