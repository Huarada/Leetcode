int romanToInt(char * s){
    int dec = 0;
    int unit = 0;
    int cent = 0;
    int mil = 0;
    bool adC = true;
    bool adD = true;
    bool adU = true;
    for (int i = 0; (int )s[i] != 0; i++)
    {
 
        adC = true;
        adD = true;
        adU = true;

        if(s[i] == 'I')
        {
            if( ((int) s[i + 1] != 0))
            {
                if (s[i + 1] == 'V')
                {
                    unit = unit +4;
                    i = i + 1;
                    adU = false;
                }
                else if (s[i + 1] == 'X')
                {
                    unit = unit + 9;
                    i = i + 1;
                    adU = false;
                }
            }
            if(adU) unit++;
        }

        if(s[i] == 'X' && adU)
        {
            if( ((int) s[i + 1] != 0))
            {
                if (s[i + 1] == 'L')
                {
                    dec = dec +4;
                    i = i + 1;
                    adD = false;
                }
                else if (s[i + 1] == 'C')
                {
                    dec = dec + 9;
                    i = i + 1;
                    adD = false;

                }
            }
            if(adD) dec++;
        
        }

  

        if(s[i] == 'V' && adU)
        {
  
            unit = unit + 5;
        }


        if(s[i] == 'C' && adD)
        {
            if( ((int) s[i + 1] != 0))
            {
                if (s[i + 1] == 'D')
                {
                    cent = cent +4;
                    i = i + 1;
                    adC = false;
                }
                else if (s[i + 1] == 'M')
                {

                    cent = cent + 9;
                    i = i + 1;
                    adC = false;


                }
            }
            if(adC) cent++;
        
        }

        if(s[i] == 'D' && adC)
        {
            cent = cent + 5;
        }
        if(s[i] == 'M' && adC )
        {
            mil ++;
        }
        if(s[i] == 'L' && adD)
        {
            dec = dec + 5;
        }

    }

    dec = dec + (unit/10);
    unit = unit % 10;

    cent = cent + (dec/10);
    dec = dec % 10;

    mil = mil + (cent/10);
    cent = cent % 10;

    int sum = 1000*mil + 100*cent + 10*dec + unit;
    return sum;
}