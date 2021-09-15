
# Maven
## Bugs
### The declared package doesn't match the expected package ...
If your files are already in the correct directory, press F1 and type in "Clean the Java Language Server Workspace"
### java.lang.NoClassDefFoundError
- Cannot find class file, need to build JAR with dependencies:
- Use maven assembly or shade
1. Add plugin to pom.xml, change `<mainClass>` tag as necessary.
```
<!--use maven assembly to create fat jar-->
        <plugin>
          <groupId>org.apache.maven.plugins</groupId>
          <artifactId>maven-assembly-plugin</artifactId>
          <configuration>
            <descriptorRefs>
              <descriptorRef>jar-with-dependencies</descriptorRef>
            </descriptorRefs>
            <archive>
              <manifest>
                <mainClass>com.mycompany.app.App</mainClass>
              </manifest>
            </archive>
          </configuration>
          <executions>
            <execution>
              <phase>package</phase>
              <goals>
                <goal>single</goal>
              </goals>
            </execution>
          </executions>
        </plugin>
```
2. Run `mvn clean compile assembly:single`
3. Run `java -cp target/nft_vehicles-1.0-SNAPSHOT-jar-with-dependencies.jar com.mycompany.app.App`