import java.io.File;
import java.nio.file.*;

public class FileOrganizer {
    public static void main(String[] args) {
        String folderPath = "C:\\Users\\YourName\\Downloads"; // change this
        organize(folderPath);
        System.out.println("Folder organized!");
    }

    public static void organize(String path) {
        File folder = new File(path);
        File[] files = folder.listFiles();
        if (files == null) return;

        for (File file : files) {
            if (file.isFile()) {
                String ext = getExtension(file.getName());
                String folderName = getFolder(ext);
                
                File newFolder = new File(path + "\\" + folderName);
                if (!newFolder.exists()) newFolder.mkdir();
                
                file.renameTo(new File(newFolder, file.getName()));
            }
        }
    }

    static String getExtension(String name) {
        int i = name.lastIndexOf('.');
        return i > 0 ? name.substring(i).toLowerCase() : "";
    }

    static String getFolder(String ext) {
        return switch(ext) {
            case ".jpg", ".png", ".jpeg" -> "Images";
            case ".pdf", ".docx", ".txt" -> "Docs";
            case ".mp4", ".mkv" -> "Videos";
            case ".java", ".py", ".cpp" -> "Code";
            case ".zip", ".rar"
