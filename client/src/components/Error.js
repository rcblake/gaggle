import Alert from "@mui/material/Alert";
import Stack from "@mui/material/Stack";

export default function Error({ msg }) {
  return (
    <Stack sx={{ width: "100%" }} spacing={2}>
      <Alert severity="error">{msg}</Alert>
    </Stack>
  );
}
