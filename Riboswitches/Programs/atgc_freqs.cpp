#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
	if(argc >= 2) {
		unsigned long nuc_count = 0;
		unsigned long a_count = 0;
		unsigned long t_count = 0;
		unsigned long g_count = 0;
		unsigned long c_count = 0;

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
		        	if(c == 'A')
		        		a_count++;
				else if(c == 'T')
					t_count++;
				else if(c == 'G')
					g_count++;
				else if(c == 'C')
					c_count++;

		        	nuc_count++;
		        }
	        }
	    }

	    fclose(f);

	    printf("%.2f\t", double(a_count) / nuc_count);
	    printf("%.2f\t", double(t_count) / nuc_count);
	    printf("%.2f\t", double(g_count) / nuc_count);
	    printf("%.2f", double(c_count) / nuc_count);

	} else {
		printf("[ERROR] Filename not provided.\n");
	}
	
	return 0;
}