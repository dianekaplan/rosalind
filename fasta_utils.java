package rosalind;

/**
 * Created by Diane on 10/9/2016.
 */

import com.sun.deploy.util.StringUtils;

import java.io.*; import java.util.*; // for reading files

public class fasta_utils {


    protected static int test() {
        // k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

        int test = 4;
        return test;
    }


    /**
     * Open and read a file, and return the lines in the file as a list
     * of Strings.
     * (Demonstrates Java FileReader, BufferedReader, and Java5.)
     *
     * Modified this: http://alvinalexander.com/blog/post/java/how-open-read-file-java-string-array-list
     */

    protected static List<String> readFile(String filename)
    {

        boolean DEBUG = false;

        List<String> records = new ArrayList<String>();
        try
        {
            BufferedReader reader = new BufferedReader(new FileReader(filename));
            String line;
            String this_seq = "";

            while ((line = reader.readLine()) != null)
            {
                // If the line is a new fasta sequence, save any current string and start a new one
                if (line.startsWith(">")) {
                    // If we have one in progress, save it
                    if (this_seq.length() != 0) {
                        if (DEBUG) {System.out.println("Adding seq: " + this_seq);}
                        records.add(this_seq);
                    }
                    // Start a new variable with this line
                    this_seq = line;
                }

                // If we're in the middle of a sequence, just append it
                else {
                    this_seq += line;
                }

            }
            // save off the last one
            records.add(this_seq);
            reader.close();

            return records;
        }
        catch (Exception e)
        {
            System.err.format("Exception occurred trying to read '%s'.", filename);
            e.printStackTrace();
            return null;
        }
    }

    protected static List<String>  get_seq_strings (String file_name)
    {
        // Declare cleaned list
        List<String> cleaned_list = new ArrayList<String>();

        // Get the list of strings from the file
        List<String> seq_list =  readFile (file_name);



        // Strip off the fasta header to keep only the sequence bases
        for( String seq : seq_list ) {
            seq = clean_fasta_string(seq);
            cleaned_list.add(seq);
        }

        return cleaned_list;
    }


    protected static String clean_fasta_string (String messy_string)
    {
        // Only keep the sequence itself (strips off heading line like >Rosalind_3529
        String cleaned_string = messy_string.replaceAll("[^A,C,G,T]", "");

        return cleaned_string;
    }

}
