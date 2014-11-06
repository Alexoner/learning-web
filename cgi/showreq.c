/*************************************************************************
    > File Name: showreq.c
    > Author: onerhao
    > Mail: haodu@hustunique.com
    > Created Time: Sat 20 Jul 2013 01:10:34 AM EDT
 ************************************************************************/
/**
 * This CGI script print the request of which the method is "POST"
 */
#include <stdio.h>
#include <stdlib.h>
int main()
{
	int i,n;
	printf ("Content-Type:text/plain\r\n\r\n");
	n=0;
	if(getenv("CONTENT_LENGTH"))
		n=atoi(getenv("CONTENT_LENGTH"));
	if(n)
	{
		for (i=0; i<n; i++)
		{
			putchar(getchar());
		}
		putchar('\n');
	}
	else
	{
		printf("%s",getenv("QUERY_STRING"));
	}
	printf("CONTENT_LENGTH:%d\n",n);
	fflush(stdout);
}
