void leakseverywhere(void)
{
	float *a = malloc(sizeof(float) * 45);
}

int main(void)
{
	leakseverywhere();
}
