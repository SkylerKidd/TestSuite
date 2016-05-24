import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonElement;
import com.google.gson.JsonParser;

/**
 * Created by norelltagle on 5/22/16.
 */
public class Test {

    public static void main(String[] args) {


        JsonParser parser = new JsonParser();
        Gson gson = new GsonBuilder().setPrettyPrinting().create();

        String json = "\"{\"a\":1,\"b\":2,\"c\":{\"d\":1,\"e\":[1,2]}}\"";

        JsonElement el = parser.parse(json);

        json = gson.toJson(el);

        System.out.println(json);


    }
}
