/*************************************************************************
    > File Name: get.c
    > Author: onerhao
    > Mail: haodu@hustunique.com
    > Created Time: Sat 31 Aug 2013 08:59:16 PM CST
 ************************************************************************/

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main()
{
	char *method=getenv("REQUEST_METHOD");
	char *data;

	printf("Content-type: text/plain\n\n");//generate header

	if(method&&strcmp(method,"GET")==0)
	{
		data=getenv("QUERY_STRING");
		printf("%s\n",data);
	}
	else if(method&&strcmp(method,"POST")==0)
	{
		;
	}
	return 0;
}
