import java.util.Arrays;

public class quicksort {
    public static void main(String[] args) {
        int[] arr = {13,19,9,5,12,8,7,4,21,2,6,11};
        sort(arr, 0, arr.length-1);
        System.out.println(Arrays.toString(arr));
    }

    private static void sort(int[] arr, int start, int end) {
        // attention: the divide-and-conquer algorithm should satisfy 
        // this requirement: start<end. The number of elements is 2 or more
        if(start<end) {
            int pilot = partition(arr, start, end);
            sort(arr, start, pilot-1);
            sort(arr, pilot+1, end);
        }
    }

    private static int partition(int[] arr, int start, int end) {
        int i = start;
        for(int j=start;j<end;j++) {
            // if we scan a element arr[j] smaller than arr[end],
            // then we write it to arr[i], and move the old arr[i] to arr[j]
            // This is a two-pointer solution to this problem
            if(arr[j]<arr[end]) {
                swap(arr, i, j);
                i++;
            }
        }
        // put the last element to i-th position, then return i-index. 
        swap(arr, i, end);
        return i;
    }

    private static void swap(int[] arr, int i, int j) {
        int tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }
}