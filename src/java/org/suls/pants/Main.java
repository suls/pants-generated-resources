package org.suls.pants;

import java.io.IOException;
import java.io.InputStream;
import java.util.Optional;
import java.util.Properties;

public class Main {
    public static void main(String[] args) {
        Properties properties = new Properties();

        Optional<InputStream> stream = Optional.ofNullable(Main.class.getClassLoader().getResourceAsStream("/generated.properties"));
        stream.map(s -> {
            try {
                properties.load(s);
            } catch (IOException e) {
                e.printStackTrace();
            }
            return properties;
        });

        System.out.printf("hello, %s!", properties.getProperty("who", "unknown"));
    }
}
