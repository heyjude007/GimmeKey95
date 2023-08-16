# GimmeKey95
A product key generator for Windows 95.
## How does this work?
This works because of how Windows 95 Product Keys work.  
Windows 95's Product Key structure is slightly different depending on whether it is a Retail or OEM key.  
### Retail Keys
Let's take a Retail Key as an example: 219-3011011  
**The first three digits (219) are a prefix.  
This can be any number, as long as it isn't equal to 222, 333, 444, 555, 666, 777, 888, or 999.  
The fourth character (-) is unchecked. This can be any character.  
The last 7 digits (3011011) are numbers between 0-8, the sum of which must be divisible by 7 with no remainder.**  
It is for this reason that 111-1111111 and 000-0000007 are valid product keys, as the first three digits arent equal to the previously mentioned numbers, and the last 7 digits are divisable by 7 with no remainder.
### OEM Keys
Let's take an OEM key as an example: 18896-OEM-0023101-69682  
**The first five digits are the day that the key was printed. The first three digits (188) is the day and the next two (96) are the year, which implies that this particular key (18896) was printed on the 6th of July 1996.  
The year has to be between 1995 and 2003 otherwise the key returns invalid.  
The next three characters are always OEM.  
The next 7 digits follow the same rule as the retail keys, in that the sum of the digits has to be divisable by 7 with no remainder, except the first two digits must be 00.  
The next 5 digits aren't relevant as long as there are 5 digits there.**  
## Is this even legal?
Kind of. Strictly speaking, Microsoft does own the copyright for windows 95, which means it is considered piracy and is illegal.  
But since Windows 95 is abandonware and Microsoft no longer make money from it and hasn't for almost 20 years the only way to get Windows 95 anymore is by piracy or buying used media, neither of which earn Microsoft any money.  
So while it is technically unlawful, it isn't unethical.  
### **_FOR THE RECORD THIS IS NOT LEGAL ADVICE, I AM NOT A LAWYER, JUST SOMEONE WHO DID A BIT OF READING. I WILL NOT BE HELD RESPONSIBLE IF YOU GET IN TROUBLE FOR USING THIS PROGRAM._**
## Do the codes also work for Microsoft Office 95?
Theoretically yes, but I haven't tested it on Office 95.  
## How much help did you get from ChatGPT?
Quite a bit. I made this a while ago, and I was less proficient in Python then.  
ChatGPT did the GUI programming with Tkinter and some of the code generation side as well.  



