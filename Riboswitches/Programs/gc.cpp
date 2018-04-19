#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
	if(argc >= 2) {
		unsigned long nuc_count = 0;
		unsigned long gc_count = 0;

		bool checkForNewLine = false;
		FILE *f;
	    char c;
	    f=fopen(argv[1],"rt");

	    while((c=fgetc(f)) != EOF){
	        if(c == '>')
	        	checkForNewLine = true;

	        if(c == '\n') {
	        	checkForNewLine = false;
	        } else {
	        	if(!checkForNewLine) {
		        	if(c == 'G' || c == 'C')
		        		gc_count++;

		        	nuc_count++;
		        }
	        }
	    }

	    fclose(f);

	    printf("%F", double(gc_count * 100.0f / nuc_count));

	} else {
		printf("[ERROR] Filename not provided.\n");
	}
	
	return 0;
}