using System.Collections.Generic;
using System.IO;
using Newtonsoft.Json.Linq;
using Newtonsoft.Json.Schema;
using Newtonsoft.Json;

namespace FhirApp
{
    public class ValidationResult
    {
        public ValidationResult(bool valid, IList<string> errors)
        {
            Valid = valid;
            Errors = errors;
        }

        public bool Valid { get; }
        public IList<string> Errors { get; }

    }

    public class FhirJsonValidator
    {
        private readonly JSchema schema;

        public FhirJsonValidator(string schemaPath)
        {
            JsonTextReader reader = new JsonTextReader(new StreamReader(schemaPath));
            schema = JSchema.Load(reader);
        }

        public ValidationResult ValidateSchema(string resoursePath)
        {
            JsonTextReader reader = new JsonTextReader(new StreamReader(resoursePath));
            JObject resourse = JObject.Load(reader);
            IList<string> errors;
            bool valid = resourse.IsValid(schema, out errors);

            return new ValidationResult(valid, errors);
        }

    }
}
