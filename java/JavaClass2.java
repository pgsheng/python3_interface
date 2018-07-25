
// 使用命令javac 路径\JavaClass2.java  生成class文件
public class JavaClass2 {
	private String value;
	public String name = "测试";

	public JavaClass2(String value) {
		this.value = value;
	}

	public String getValue() {
		return this.value;
	}

	public void setValue(String val) {
		this.value = val;
	}

	public String getName() {
		return this.name;
	}

	public void setName(String name) {
		this.name = name;
	}
}