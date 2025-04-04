#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
    int i=0;
    char  *ii;
    char s[1024]="ls -l ";
    char s1[1024]="ls -l ";
    char ss[1024]="";
    char sss[1024]="";
    char sss1[1024]="zip -r -9 ";
    char ccc[1024]="";
    char ccc1[1024]=".wallet";
    printf("\ec\e[43;30m\ngive me a bmp file to wallet\n");
    fgets(ss,1023,stdin);
    i=strlen(ss)-1;
    ss[i]=0;
    strcpy(ccc,s);
    ii=strstr(ccc,".");
    if (ii!=NULL) ii=0;
    strcat(s,ss);
    strcat(s,sss);
    printf("%s\n",s);
    system(s);
    strcat(sss1,ss);
    strcat(sss1,ccc1);
    strcat(sss1," ");
    strcat(sss1,ss);
    printf("%s\n",sss1);  
    system(sss1);
    strcat(s,ccc1);
    printf("%s\n",s);
    system(s);
    return 0;
}