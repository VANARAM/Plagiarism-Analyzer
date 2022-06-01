import java.util.*;
import java.io.*;
class Test implements Serializable {
	String name;
	String city;
	int age;
	Test(String name,String city,int age){
		this.name = name;
		this.city = city;
		this.age = age;
	}
	public String toString(){
		return name+" "+city+" "+age;
	}
}
public class vn
{
	public static void main(String args[]) throws IOException, ClassNotFoundException
	{
		Test t1 = new Test("vana","navsari",20);
		Test t2 = new Test("noel","valsad",21);
		ArrayList<Test> test = new ArrayList<>();
		test.add(t1);
		test.add(t2);
		System.out.println(test);
		
		FileOutputStream fos = new FileOutputStream("vn.txt");
		ObjectOutputStream oos = new ObjectOutputStream(fos);
		oos.writeObject(test);
		System.out.println("finish");
		oos.close();
		fos.close();
		
		FileInputStream fis = new FileInputStream("vn.txt");
		ObjectInputStream ois = new ObjectInputStream(fis);
		//ArrayList<Test> test = new ArrayList<>();
		//test = (ArrayList<Test>)ois.readObject();
		Object obj = ois.readObject();
		System.out.println("readed");
		System.out.println(obj);
		/*for(Test ts:test){
			System.out.println(ts);
		}*/
	}
}