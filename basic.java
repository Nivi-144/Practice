int left = 0;
int sum = 0;
for (int right = 0; right < arr.length; right++) {
    sum += arr[right];
    if (right - left + 1 == k) {
        System.out.println(sum);
        sum -= arr[left];
        left++;
    }
}
