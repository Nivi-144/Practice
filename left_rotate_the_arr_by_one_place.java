class left_rotate_the_arr_by_D_place_brute{
    public static void main(String args[]){
        int[] arr={1,2,3,4,5,6,7};
        int d=3;
        int[] temp =new int[d];
        int n=arr.length;
        d=d%n;
        for(int i=0;i<d;i++){
            temp[i]=arr[i];
            i++;
        }
        for(int i=d;i<n;i++){
            arr[i-d]=arr[i];
        }
        for(int i=n-d;i<n;i++){
            arr[i]=temp[i-(n-d)];  
        }
        System.out.print("Rotated Array:");
        for(int i=0;i<n;i++){
            Syatem.out.println(arr[i]+" ");
        }
        
    }
}