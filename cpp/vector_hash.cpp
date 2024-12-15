#include <cstdlib>
#include <ctime>
#include <vector>
#include <iostream>

using namespace std;

class VectorHash {
public:
    VectorHash(vector<int>& nums) {
        // define rand variables
        srand(time(NULL));
        BASE1 = 8 * (long long)1e8 + rand() % (long long)1e8 + 100;
        BASE2 = 8 * (long long)1e8 + rand() % (long long)1e8;
        MOD = (long long) 1e9 + 7;
        // initialize data structures
        pre_hash1 = vector<long long>(nums.size());
        base_pow1 = vector<long long>(nums.size()+1);
        pre_hash2 = vector<long long>(nums.size());
        base_pow2 = vector<long long>(nums.size()+1);
        // initialize values in vectors
        init_hash(nums);
    }
    // get hash value from haystack's substring including start and end points
    long long get_substr_hash(int start, int end) {
        if(start == 0) {
            return (pre_hash1[end] << 32 | pre_hash2[end]);
        } else {
            long long res1 = (pre_hash1[end] - pre_hash1[start-1] * base_pow1[end-start+1] % MOD + MOD) % MOD;
            long long res2 = (pre_hash2[end] - pre_hash2[start-1] * base_pow2[end-start+1] % MOD + MOD) % MOD;
            return (res1 << 32 | res2);
        }
    }
    // get a new string's hash value
    long long get_str_hash(vector<int>& needle) {
        long long hash1 = 0, hash2 = 0;
        for(int i=0;i<needle.size();i++) {
            int val = needle[i];
            hash1 = (hash1 * BASE1 + val) % MOD;
        }
        for(int i=0;i<needle.size();i++) {
            int val = needle[i];
            hash2 = (hash2 * BASE2 + val) % MOD;
        }
        return (hash1 << 32 | hash2);
    }

private:
    // global variables
    vector<long long> pre_hash1;
    vector<long long> base_pow1;
    vector<long long> pre_hash2;
    vector<long long> base_pow2;
    long long BASE1;
    long long BASE2;
    long long MOD;

    // initialize haystack's hash values in prefix arrays
    void init_hash(vector<int>& haystack) {
        // encode hash1
        for(int i=0;i<haystack.size();i++) {
            int val = haystack[i];
            if(i==0) {
                pre_hash1[i] = val;
                base_pow1[i] = 1;
            } else {
                pre_hash1[i] = (pre_hash1[i-1] * BASE1 + val) % MOD;
                base_pow1[i] = (base_pow1[i-1] * BASE1) % MOD;
            }
        }
        base_pow1[haystack.size()] = (base_pow1[haystack.size()-1] * BASE1) % MOD;
        // encode hash2
        for(int i=0;i<haystack.size();i++) {
            int val = haystack[i];
            if(i==0) {
                pre_hash2[i] = val;
                base_pow2[i] = 1;
            } else {
                pre_hash2[i] = (pre_hash2[i-1] * BASE2 + val) % MOD;
                base_pow2[i] = (base_pow2[i-1] * BASE2) % MOD;
            }
        }
        base_pow2[haystack.size()] = (base_pow2[haystack.size()-1] * BASE2) % MOD;
    }
};

int main() {
    vector<int> nums = {1,1,2,1,2,3};
    vector<int> b = {1};
    VectorHash vh(nums);
    // get the hash value for a new word
    long long target = vh.get_str_hash(b);
    // they should be the same
    cout << target << endl;
    cout << vh.get_substr_hash(0,0) << endl;
    cout << vh.get_substr_hash(1,1) << endl;
    cout << vh.get_substr_hash(3,3) << endl;
}