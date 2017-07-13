using System;
using FhirApp;
using System.IO;

namespace ValidationTest
{
    class Program
    {
        static void Main(string[] args)
        {
            if (args.Length != 2)
            {
                Console.WriteLine("Enter the path to schema and resource.");
                return;
            }

            try
            {
                FhirJsonValidator v = new FhirJsonValidator(args[0]);
                ValidationResult res = v.ValidateSchema(args[1]);
                Console.WriteLine(string.Format("Validating: {0}", args[1]));
                if (res.Valid)
                {
                    Console.WriteLine("Resourse is valid.");
                }
                else
                {
                    foreach (string s in res.Errors)
                    {
                        Console.WriteLine(s);
                    }
                }
            }
            catch (IOException e)
            {
                Console.WriteLine(e.Message);
                return;
            }
        }
    }

}


