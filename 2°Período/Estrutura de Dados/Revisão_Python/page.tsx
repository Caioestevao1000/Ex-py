const prepareDailyReport = (data: DailyReportType[]) => {
  if (!data || data.length === 0) return [];

  const totalDays = data.length;

  let groupSize = 1;
  let mode: "daily" | "weekly" | "biweekly" | "monthly" = "daily";

  if (totalDays > 31 && totalDays <= 92) {
    groupSize = 7;
    mode = "weekly";
  } else if (totalDays > 92 && totalDays <= 365) {
    groupSize = 15;
    mode = "biweekly";
  } else if (totalDays > 365) {
    mode = "monthly";
  }

  if (mode === "daily") {
    return data.map((d) => ({
      ...d,
      date: new Date(d.date).getUTCDate().toString(),
    }));
  }

  if (mode === "monthly") {
    const groups: Record<string, DailyReportType> = {};

    data.forEach((d) => {
      const date = new Date(d.date);
      const month = (date.getUTCMonth() + 1).toString().padStart(2, "0");
      const year = date.getUTCFullYear().toString();
      const key = `${month}/${year}`;

      if (!groups[key]) {
        groups[key] = { date: key, views: 0, answers: 0 };
      }

      groups[key].views += d.views;
      groups[key].answers += d.answers;
    });

    return Object.values(groups);
  }

  let viewsAccumulator = 0;
  let answersAccumulator = 0;
  let resp: DailyReportType[] = [];

  for (let i = 0; i < data.length; i++) {
    viewsAccumulator += data[i].views;
    answersAccumulator += data[i].answers;

    const isLast = i === data.length - 1;
    const isGroupBoundary = (i + 1) % groupSize === 0 || isLast;

    if (isGroupBoundary) {
      const date = new Date(data[i].date);
      const day = date.getUTCDate().toString().padStart(2, "0");
      const month = (date.getUTCMonth() + 1).toString().padStart(2, "0");
      const label = `${day}/${month}`;

      resp.push({
        date: label,
        views: viewsAccumulator,
        answers: answersAccumulator,
      });

      viewsAccumulator = 0;
      answersAccumulator = 0;
    }
  }

  return resp;
};