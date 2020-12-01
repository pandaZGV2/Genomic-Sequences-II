  #include <stdio.h>
  int main(void)
   {       
          FILE *fptr,*fptr2;
          fptr=fopen("out1.txt","r");
          fptr2=fopen("out2.txt","r");
          char n,c;
          while(fscanf(fptr,"%c",&n)==1 && fscanf(fptr2,"%c",&c)==1)
          {       
                 if(n==c)
                         continue;
                else
                 {       
                       printf("%c %c\n",n,c);
                 }       
}
         return 0;
 }       

