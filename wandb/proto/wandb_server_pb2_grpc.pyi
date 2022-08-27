"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import wandb.proto.wandb_internal_pb2
import wandb.proto.wandb_telemetry_pb2

from .wandb_server_pb2 import *
class InternalServiceStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    def RunUpdate(self,
        request: wandb.proto.wandb_internal_pb2.RunRecord,
    ) -> wandb.proto.wandb_internal_pb2.RunUpdateResult: ...

    def Attach(self,
        request: wandb.proto.wandb_internal_pb2.AttachRequest,
    ) -> wandb.proto.wandb_internal_pb2.AttachResponse: ...

    def TBSend(self,
        request: wandb.proto.wandb_internal_pb2.TBRecord,
    ) -> wandb.proto.wandb_internal_pb2.TBResult: ...

    def RunStart(self,
        request: wandb.proto.wandb_internal_pb2.RunStartRequest,
    ) -> wandb.proto.wandb_internal_pb2.RunStartResponse: ...

    def GetSummary(self,
        request: wandb.proto.wandb_internal_pb2.GetSummaryRequest,
    ) -> wandb.proto.wandb_internal_pb2.GetSummaryResponse: ...

    def SampledHistory(self,
        request: wandb.proto.wandb_internal_pb2.SampledHistoryRequest,
    ) -> wandb.proto.wandb_internal_pb2.SampledHistoryResponse: ...

    def PollExit(self,
        request: wandb.proto.wandb_internal_pb2.PollExitRequest,
    ) -> wandb.proto.wandb_internal_pb2.PollExitResponse: ...

    def ServerInfo(self,
        request: wandb.proto.wandb_internal_pb2.ServerInfoRequest,
    ) -> wandb.proto.wandb_internal_pb2.ServerInfoResponse: ...

    def Shutdown(self,
        request: wandb.proto.wandb_internal_pb2.ShutdownRequest,
    ) -> wandb.proto.wandb_internal_pb2.ShutdownResponse: ...

    def RunExit(self,
        request: wandb.proto.wandb_internal_pb2.RunExitRecord,
    ) -> wandb.proto.wandb_internal_pb2.RunExitResult: ...

    def RunPreempting(self,
        request: wandb.proto.wandb_internal_pb2.RunPreemptingRecord,
    ) -> wandb.proto.wandb_internal_pb2.RunPreemptingResult: ...

    def Metric(self,
        request: wandb.proto.wandb_internal_pb2.MetricRecord,
    ) -> wandb.proto.wandb_internal_pb2.MetricResult: ...

    def PartialLog(self,
        request: wandb.proto.wandb_internal_pb2.PartialHistoryRequest,
    ) -> wandb.proto.wandb_internal_pb2.PartialHistoryResponse: ...

    def Log(self,
        request: wandb.proto.wandb_internal_pb2.HistoryRecord,
    ) -> wandb.proto.wandb_internal_pb2.HistoryResult: ...

    def Summary(self,
        request: wandb.proto.wandb_internal_pb2.SummaryRecord,
    ) -> wandb.proto.wandb_internal_pb2.SummaryResult: ...

    def Config(self,
        request: wandb.proto.wandb_internal_pb2.ConfigRecord,
    ) -> wandb.proto.wandb_internal_pb2.ConfigResult: ...

    def Files(self,
        request: wandb.proto.wandb_internal_pb2.FilesRecord,
    ) -> wandb.proto.wandb_internal_pb2.FilesResult: ...

    def Output(self,
        request: wandb.proto.wandb_internal_pb2.OutputRecord,
    ) -> wandb.proto.wandb_internal_pb2.OutputResult: ...

    def OutputRaw(self,
        request: wandb.proto.wandb_internal_pb2.OutputRawRecord,
    ) -> wandb.proto.wandb_internal_pb2.OutputRawResult: ...

    def Telemetry(self,
        request: wandb.proto.wandb_telemetry_pb2.TelemetryRecord,
    ) -> wandb.proto.wandb_telemetry_pb2.TelemetryResult: ...

    def Alert(self,
        request: wandb.proto.wandb_internal_pb2.AlertRecord,
    ) -> wandb.proto.wandb_internal_pb2.AlertResult: ...

    def Artifact(self,
        request: wandb.proto.wandb_internal_pb2.ArtifactRecord,
    ) -> wandb.proto.wandb_internal_pb2.ArtifactResult: ...

    def LinkArtifact(self,
        request: wandb.proto.wandb_internal_pb2.LinkArtifactRecord,
    ) -> wandb.proto.wandb_internal_pb2.LinkArtifactResult: ...

    def ArtifactSend(self,
        request: wandb.proto.wandb_internal_pb2.ArtifactSendRequest,
    ) -> wandb.proto.wandb_internal_pb2.ArtifactSendResponse: ...

    def ArtifactPoll(self,
        request: wandb.proto.wandb_internal_pb2.ArtifactPollRequest,
    ) -> wandb.proto.wandb_internal_pb2.ArtifactPollResponse: ...

    def KeepAlive(self,
        request: wandb.proto.wandb_internal_pb2.KeepAliveRequest,
    ) -> wandb.proto.wandb_internal_pb2.KeepAliveResponse: ...

    def CheckVersion(self,
        request: wandb.proto.wandb_internal_pb2.CheckVersionRequest,
    ) -> wandb.proto.wandb_internal_pb2.CheckVersionResponse: ...

    def Pause(self,
        request: wandb.proto.wandb_internal_pb2.PauseRequest,
    ) -> wandb.proto.wandb_internal_pb2.PauseResponse: ...

    def Resume(self,
        request: wandb.proto.wandb_internal_pb2.ResumeRequest,
    ) -> wandb.proto.wandb_internal_pb2.ResumeResponse: ...

    def Status(self,
        request: wandb.proto.wandb_internal_pb2.StatusRequest,
    ) -> wandb.proto.wandb_internal_pb2.StatusResponse: ...

    def ServerShutdown(self,
        request: global___ServerShutdownRequest,
    ) -> global___ServerShutdownResponse: ...

    def ServerStatus(self,
        request: global___ServerStatusRequest,
    ) -> global___ServerStatusResponse: ...

    def ServerInformInit(self,
        request: global___ServerInformInitRequest,
    ) -> global___ServerInformInitResponse: ...

    def ServerInformStart(self,
        request: global___ServerInformStartRequest,
    ) -> global___ServerInformStartResponse: ...

    def ServerInformFinish(self,
        request: global___ServerInformFinishRequest,
    ) -> global___ServerInformFinishResponse: ...

    def ServerInformAttach(self,
        request: global___ServerInformAttachRequest,
    ) -> global___ServerInformAttachResponse: ...

    def ServerInformDetach(self,
        request: global___ServerInformDetachRequest,
    ) -> global___ServerInformDetachResponse: ...

    def ServerInformTeardown(self,
        request: global___ServerInformTeardownRequest,
    ) -> global___ServerInformTeardownResponse: ...


class InternalServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def RunUpdate(self,
        request: wandb.proto.wandb_internal_pb2.RunRecord,
        context: grpc.ServicerContext,
    ) -> wandb.proto.wandb_internal_pb2.RunUpdateResult: ...

    @abc.abstractmethod
    def Attach(self,
        request: wandb.proto.wandb_internal_pb2.AttachRequest,
        context: grpc.ServicerContext,
    ) -> wandb.proto.wandb_internal_pb2.AttachResponse: ...

    @abc.abstractmethod
    def TBSend(self,
        request: wandb.proto.wandb_internal_pb2.TBRecord,
        context: grpc.ServicerContext,
    ) -> wandb.proto.wandb_internal_pb2.TBResult: ...

    @abc.abstractmethod
    def RunStart(self,
        request: wandb.proto.wandb_internal_pb2.RunStartRequest,
        context: grpc.ServicerContext,
    ) -> wandb.proto.wandb_internal_pb2.RunStartResponse: ...

    @abc.abstractmethod
    def GetSummary(self,
        request: wandb.proto.wandb_internal_pb2.GetSummaryRequest,
        context: grpc.ServicerContext,
    ) -> wandb.proto.wandb_internal_pb2.GetSummaryResponse: ...

    @abc.abstractmethod
    def SampledHistory(self,
        request: wandb.proto.wandb_internal_pb2.SampledHistoryRequest,
        context: grpc.ServicerContext,
    ) -> wandb.proto.wandb_internal_pb2.SampledHistoryResponse: ...

    @abc.abstractmethod
    def PollExit(self,
        request: wandb.proto.wandb_internal_pb2.PollExitRequest,
        context: grpc.ServicerContext,
    ) -> wandb.proto.wandb_internal_pb2.PollExitResponse: ...

    @abc.abstractmethod
    def ServerInfo(self,
        request: wandb.proto.wandb_internal_pb2.ServerInfoRequest,
        context: grpc.ServicerContext,
    ) -> wandb.proto.wandb_internal_pb2.ServerInfoResponse: ...

    @abc.abstractmethod
    def Shutdown(self,
        request: wandb.proto.wandb_internal_pb2.ShutdownRequest,
        context: grpc.ServicerContext,
    ) -> wandb.proto.wandb_internal_pb2.ShutdownResponse: ...

    @abc.abstractmethod
    def RunExit(self,
        request: wandb.proto.wandb_internal_pb2.RunExitRecord,
        context: grpc.ServicerContext,
    ) -> wandb.proto.wandb_internal_pb2.RunExitResult: ...

    @abc.abstractmethod
    def RunPreempting(self,
        request: wandb.proto.wandb_internal_pb2.RunPreemptingRecord,
        context: grpc.ServicerContext,
    ) -> wandb.proto.wandb_internal_pb2.RunPreemptingResult: ...

    @abc.abstractmethod
    def Metric(self,
        request: wandb.proto.wandb_internal_pb2.MetricRecord,
        context: grpc.ServicerContext,
    ) -> wandb.proto.wandb_internal_pb2.MetricResult: ...

    @abc.abstractmethod
    def PartialLog(self,
        request: wandb.proto.wandb_internal_pb2.PartialHistoryRequest,
        context: grpc.ServicerContext,
    ) -> wandb.proto.wandb_internal_pb2.PartialHistoryResponse: ...

    @abc.abstractmethod
    def Log(self,
        request: wandb.proto.wandb_internal_pb2.HistoryRecord,
        context: grpc.ServicerContext,
    ) -> wandb.proto.wandb_internal_pb2.HistoryResult: ...

    @abc.abstractmethod
    def Summary(self,
        request: wandb.proto.wandb_internal_pb2.SummaryRecord,
        context: grpc.ServicerContext,
    ) -> wandb.proto.wandb_internal_pb2.SummaryResult: ...

    @abc.abstractmethod
    def Config(self,
        request: wandb.proto.wandb_internal_pb2.ConfigRecord,
        context: grpc.ServicerContext,
    ) -> wandb.proto.wandb_internal_pb2.ConfigResult: ...

    @abc.abstractmethod
    def Files(self,
        request: wandb.proto.wandb_internal_pb2.FilesRecord,
        context: grpc.ServicerContext,
    ) -> wandb.proto.wandb_internal_pb2.FilesResult: ...

    @abc.abstractmethod
    def Output(self,
        request: wandb.proto.wandb_internal_pb2.OutputRecord,
        context: grpc.ServicerContext,
    ) -> wandb.proto.wandb_internal_pb2.OutputResult: ...

    @abc.abstractmethod
    def OutputRaw(self,
        request: wandb.proto.wandb_internal_pb2.OutputRawRecord,
        context: grpc.ServicerContext,
    ) -> wandb.proto.wandb_internal_pb2.OutputRawResult: ...

    @abc.abstractmethod
    def Telemetry(self,
        request: wandb.proto.wandb_telemetry_pb2.TelemetryRecord,
        context: grpc.ServicerContext,
    ) -> wandb.proto.wandb_telemetry_pb2.TelemetryResult: ...

    @abc.abstractmethod
    def Alert(self,
        request: wandb.proto.wandb_internal_pb2.AlertRecord,
        context: grpc.ServicerContext,
    ) -> wandb.proto.wandb_internal_pb2.AlertResult: ...

    @abc.abstractmethod
    def Artifact(self,
        request: wandb.proto.wandb_internal_pb2.ArtifactRecord,
        context: grpc.ServicerContext,
    ) -> wandb.proto.wandb_internal_pb2.ArtifactResult: ...

    @abc.abstractmethod
    def LinkArtifact(self,
        request: wandb.proto.wandb_internal_pb2.LinkArtifactRecord,
        context: grpc.ServicerContext,
    ) -> wandb.proto.wandb_internal_pb2.LinkArtifactResult: ...

    @abc.abstractmethod
    def ArtifactSend(self,
        request: wandb.proto.wandb_internal_pb2.ArtifactSendRequest,
        context: grpc.ServicerContext,
    ) -> wandb.proto.wandb_internal_pb2.ArtifactSendResponse: ...

    @abc.abstractmethod
    def ArtifactPoll(self,
        request: wandb.proto.wandb_internal_pb2.ArtifactPollRequest,
        context: grpc.ServicerContext,
    ) -> wandb.proto.wandb_internal_pb2.ArtifactPollResponse: ...

    @abc.abstractmethod
    def KeepAlive(self,
        request: wandb.proto.wandb_internal_pb2.KeepAliveRequest,
        context: grpc.ServicerContext,
    ) -> wandb.proto.wandb_internal_pb2.KeepAliveResponse: ...

    @abc.abstractmethod
    def CheckVersion(self,
        request: wandb.proto.wandb_internal_pb2.CheckVersionRequest,
        context: grpc.ServicerContext,
    ) -> wandb.proto.wandb_internal_pb2.CheckVersionResponse: ...

    @abc.abstractmethod
    def Pause(self,
        request: wandb.proto.wandb_internal_pb2.PauseRequest,
        context: grpc.ServicerContext,
    ) -> wandb.proto.wandb_internal_pb2.PauseResponse: ...

    @abc.abstractmethod
    def Resume(self,
        request: wandb.proto.wandb_internal_pb2.ResumeRequest,
        context: grpc.ServicerContext,
    ) -> wandb.proto.wandb_internal_pb2.ResumeResponse: ...

    @abc.abstractmethod
    def Status(self,
        request: wandb.proto.wandb_internal_pb2.StatusRequest,
        context: grpc.ServicerContext,
    ) -> wandb.proto.wandb_internal_pb2.StatusResponse: ...

    @abc.abstractmethod
    def ServerShutdown(self,
        request: global___ServerShutdownRequest,
        context: grpc.ServicerContext,
    ) -> global___ServerShutdownResponse: ...

    @abc.abstractmethod
    def ServerStatus(self,
        request: global___ServerStatusRequest,
        context: grpc.ServicerContext,
    ) -> global___ServerStatusResponse: ...

    @abc.abstractmethod
    def ServerInformInit(self,
        request: global___ServerInformInitRequest,
        context: grpc.ServicerContext,
    ) -> global___ServerInformInitResponse: ...

    @abc.abstractmethod
    def ServerInformStart(self,
        request: global___ServerInformStartRequest,
        context: grpc.ServicerContext,
    ) -> global___ServerInformStartResponse: ...

    @abc.abstractmethod
    def ServerInformFinish(self,
        request: global___ServerInformFinishRequest,
        context: grpc.ServicerContext,
    ) -> global___ServerInformFinishResponse: ...

    @abc.abstractmethod
    def ServerInformAttach(self,
        request: global___ServerInformAttachRequest,
        context: grpc.ServicerContext,
    ) -> global___ServerInformAttachResponse: ...

    @abc.abstractmethod
    def ServerInformDetach(self,
        request: global___ServerInformDetachRequest,
        context: grpc.ServicerContext,
    ) -> global___ServerInformDetachResponse: ...

    @abc.abstractmethod
    def ServerInformTeardown(self,
        request: global___ServerInformTeardownRequest,
        context: grpc.ServicerContext,
    ) -> global___ServerInformTeardownResponse: ...


def add_InternalServiceServicer_to_server(servicer: InternalServiceServicer, server: grpc.Server) -> None: ...
