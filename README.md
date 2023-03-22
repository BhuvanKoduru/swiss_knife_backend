SwissKnife


How to run the app:
1. install all the dependencies using the command: pip install -r requirements.txt
2. additionally, install Graphviz.
3. Once the dependencies are installed, run the "app.py" file using "python app.py" to start the Flask application.
4. By default, flask apps are run from port 5000, and the ip address is the default address for local systems, i.e, 127.0.0.1
5. Now to run the app you either require VScode or Android studio 
6. Now download the flutter SDK and other required extentions mentioned in flutter's official website 
7. Before running the app make sure the localhost is created and app.py has no errors in it 
8. Now you can use the app according to your requirements and also store your projects
9. Here are few examples that you can try using this app
   1. For the java calculator:
      "import java.io.*; import java.math.BigInteger; import java.util.InputMismatchException; import java.util.PriorityQueue; import java.util.StringTokenizer; public class D { static class FastWriter { private final BufferedWriter bw; public FastWriter() { this.bw = new BufferedWriter(new OutputStreamWriter(System.out)); } public void print(Object object) throws IOException { bw.append("" + object); } public void println(Object object) throws IOException { print(object); bw.append("\n"); } public void close() throws IOException { bw.close(); } } static class FastReader { BufferedReader br; StringTokenizer st; public FastReader() { br = new BufferedReader(new InputStreamReader(System.in)); } String next() { while (st == null || !st.hasMoreElements()) { try { st = new StringTokenizer(br.readLine()); } catch (IOException e) { e.printStackTrace(); } } return st.nextToken(); } int nextInt() { return Integer.parseInt(next()); } long nextLong() { return Long.parseLong(next()); } double nextDouble() { return Double.parseDouble(next()); } String nextLine() { String str = ""; try { str = br.readLine(); } catch (IOException e) { e.printStackTrace(); } return str; } BigInteger nextBigInteger() { try { return new BigInteger(nextLine()); } catch (NumberFormatException e) { throw new InputMismatchException(); } } } public static void main(String[] args) throws IOException { FastReader fr = new FastReader(); FastWriter fw = new FastWriter(); int n = fr.nextInt(); int m = fr.nextInt(); for (int r = 0; r < n / 2; r++) { for (int c = 0; c < m; c++) { fw.println((r + 1) + " " + (c + 1)); fw.println((n - r) + " " + (m - c)); } } if (n % 2 != 0) { int r = n / 2; for (int c = 0; c < m / 2; c++) { fw.println((r + 1) + " " + (c + 1)); fw.println((r + 1) + " " + (m - c)); } if (m % 2 != 0) fw.println((r + 1) + " " + (m / 2 + 1)); } fw.close(); } } "
      expected output: quadratic
      
    you can also run simple java code snippets like for loops:
        for(int i=0;i<5;i++)
        expected output: linear
        
   2. Python maintainability calculator:
        pass the complete path of any LOCAL python file, ex: C:\Users\User1\PythonCode\test.py
        
   3. Function call flowchart:
        similar to the python maintainability calculator, pass the complete path of a LOCAL python file. The output will be sent as an image (PNG) to an         email id of your choice.
        
   4. Malicious Commits:
        To use this feature, please pass the complete path of a PUBLIC GITHUB repository, and the corresponding output message will be displayed on               screen. Ex: https://github.com/GoogleTrends/data
     
