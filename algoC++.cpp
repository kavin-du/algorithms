#define forl(i, a, b)\
	for(int i=int(a); i<int(b); i++)

///// prime check

arr.erase(unique(arr.begin(),arr.end()),arr.end()) - This erases the duplicate occurrences in sorted vector 

#define <cmath>

bool isPrime(int n){
    if(n < 2) return false;
    forl(i, 2, (int)(sqrt(n))+1){
        if (n%i == 0){
            return false;
        }
    }
    return true;
}
