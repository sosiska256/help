import java.util.Scanner;

public class Perevod7 {
    static Scanner in = new Scanner(System.in);

    public static void main(String[] args) {
        System.out.print("Тип задачи: 1. Текстовая информация 2. Звуковая информация 3. Графическая информация: ");
        int a = 0;
        while (a == 0) {
            int N = in.nextInt();
            switch (N) {
                case 1: {
                    text(a);
                    break;
                }
                case 2: {
                    sound(a);
                    break;
                }
                case 3: {
                    photo(a);
                    break;
                }
                default:
                    System.out.println("Такого пункта нету");
                    break;
            }
        }
    }

    public static int text(int a) {
        System.out.print("Что необходимо найти? (I, K, i, N): ");
        String What = in.next();
        int K = 0;
        int i = 0;
        int N = 0;
        int I = 0;
        switch (What) {
            case "I":
                System.out.print("K = ");
                K = in.nextInt();
                System.out.print("i = ");
                i = in.nextInt();
                System.out.println("I = " + K * i);
                break;
            case "K":
                System.out.print("I = ");
                I = in.nextInt();
                System.out.print("i = ");
                i = in.nextInt();
                System.out.println("K = " + I / i);
                break;
            case "i":
                System.out.print("N = ");
                N = in.nextInt();
                if (N == 0) {
                    System.out.print("I = ");
                    I = in.nextInt();
                    System.out.print("K = ");
                    K = in.nextInt();
                    System.out.println("i = " + I / K);
                    break;
                } else {
                    System.out.println("i =" + Math.log(N));
                    break;
                }
            case "N":
                System.out.print("i = ");
                i = in.nextInt();
                System.out.println("N = " + Math.pow(2, i));
                break;
        }
        a = 1;
        return a;
    }

    public static int photo(int a) {
        System.out.print("Что необходимо найти? (V, I, M, t, k): ");
        String What = in.next();
        int V = 0;
        int I = 0;
        int M = 0;
        int t = 0;
        int k = 0;
        switch (What) {
            case "V":
                System.out.print("I = ");
                I = in.nextInt();
                System.out.print("M = ");
                M = in.nextInt();
                System.out.print("t = ");
                t = in.nextInt();
                System.out.print("k = ");
                k = in.nextInt();
                System.out.println("V = " + I * M * t * k);
                break;
            case "I":
                System.out.print("V = ");
                V = in.nextInt();
                System.out.print("M = ");
                M = in.nextInt();
                System.out.print("t = ");
                t = in.nextInt();
                System.out.print("k = ");
                k = in.nextInt();
                System.out.println("I = " + V / (M * t * k));
                break;
            case "M":
                System.out.print("V = ");
                V = in.nextInt();
                System.out.print("I = ");
                I = in.nextInt();
                System.out.print("t = ");
                t = in.nextInt();
                System.out.print("k = ");
                k = in.nextInt();
                System.out.println("I = " + V / (I * t * k));
                break;
            case "t":
                System.out.print("V = ");
                V = in.nextInt();
                System.out.print("M = ");
                M = in.nextInt();
                System.out.print("I = ");
                I = in.nextInt();
                System.out.print("k = ");
                k = in.nextInt();
                System.out.println("I = " + V / (I * M * k));
                break;
            case "k":
                System.out.print("V = ");
                V = in.nextInt();
                System.out.print("M = ");
                M = in.nextInt();
                System.out.print("I = ");
                I = in.nextInt();
                System.out.print("t = ");
                t = in.nextInt();
                System.out.println("I = " + V / (I * M * t));
                break;

        }
        a = 1;
        return a;
    }

    public static int sound(int a) {
        System.out.print("Что необходимо найти? (I, i, X, Y): ");
        String What = in.next();
        int X = 0;
        int I = 0;
        int i = 0;
        int Y = 0;
        switch (What) {
            case "i":
                System.out.print("I = ");
                I = in.nextInt();
                System.out.print("X = ");
                X = in.nextInt();
                System.out.print("Y = ");
                Y = in.nextInt();
                System.out.println("V = " + I / (X * Y));
                break;
            case "I":
                System.out.print("i = ");
                i = in.nextInt();
                System.out.print("X = ");
                X = in.nextInt();
                System.out.print("Y = ");
                Y = in.nextInt();
                System.out.println("I = " + i * X * Y);
                break;
            case "X":
                System.out.print("i = ");
                i = in.nextInt();
                System.out.print("I = ");
                I = in.nextInt();
                System.out.print("t = ");
                Y = in.nextInt();
                System.out.println("I = " + I / (i * Y));
                break;
            case "Y":
                System.out.print("X = ");
                X = in.nextInt();
                System.out.print("i = ");
                i = in.nextInt();
                System.out.print("I = ");
                I = in.nextInt();
                System.out.println("I = " + I / (i * X));
                break;
        }
        a = 1;
        return a;
    }
}