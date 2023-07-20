import Alert from "@mui/material/Alert";
import Stack from "@mui/material/Stack";

export default function Error({ msg }) {
  return (
    <Stack sx={{ width: "100%" }} spacing={2}>
      <Alert severity="error">{msg}</Alert>
    </Stack>
  );
}

// **For use at top component**
// const [errors, setErrors] = useState(null);
// **For err catch on fetch
//  res.json().then((err) => setErrors(err.error));
//
// .catch((err) => setErrors(err.error));
// **For use in components, above submit**
// {
//   errors ? <Error msg={errors} /> : null;
// }
