/*
Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function would be added by GfG's Online Judge.*/


/* The task is to complete insert() which is used 
   as shown below to implement insertionSort() */
/* Function to sort an array using insertion sort
void insertionSort(int arr[], int n)
{
   int i;
   for (i = 1; i < n; i++)
      insert(arr, i);
} */
void insert(int arr[], int i)
{
    // Your code here  
    int val = arr[i];
    int j = i;
    while(j > 0 && arr[j - 1] > val)
    {
        arr[j] = arr[j - 1];
        j -= 1;
    }
    arr[j] = val;
}

